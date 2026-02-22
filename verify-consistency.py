#!/usr/bin/env python3
"""
Agent Company v5.1 — 정합성 자동 검증 스크립트
7개 YAML + 1개 MD 파일의 교차 정합성을 20개 체크로 검증한다.
Source of Truth: agent-transitions.yaml
"""

import sys
import os
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml이 필요합니다.")
    print("  pip3 install pyyaml")
    sys.exit(2)

# ============================================================
# CONFIG
# ============================================================

BASE = Path.home() / ".claude" / "system"

FILES = {
    "transitions": BASE / "agent-transitions.yaml",
    "mutations": BASE / "state-mutations.yaml",
    "gates": BASE / "quality-gates-auto.yaml",
    "parallel": BASE / "parallel-groups.yaml",
    "io_map": BASE / "agent-io-map.yaml",
    "prompt": BASE / "prompt-assembly.yaml",
    "checkpoints": BASE / "human-checkpoints.yaml",
    "persistence": BASE / "context-persistence.md",
}

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Expected division counts
# quick_design_brief is CDO division in transitions (lightweight bridge agent)
DIVISION_COUNTS = {
    "CBO": 5,
    "CTO": 7,
    "CDO": 7,  # 6 core + quick_design_brief
    "CGO": 8,
}

# Agents exempt from certain cross-file checks (special/lightweight agents)
# quick_builder: Tier 1 only, single skill, no multi-agent structure
# quick_design_brief: lightweight bridge, inline prompt (no separate prompt-assembly)
EXEMPT_AGENTS = {"quick_builder", "quick_design_brief"}

# System files that are not agent outputs but can be in must_read
SYSTEM_FILES = {".agent-state/project.json", "project.json"}

# ============================================================
# HELPERS
# ============================================================

def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_text(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def normalize_path(p: str) -> str:
    """Remove .agent-state/outputs/ prefix for comparison."""
    p = p.strip()
    p = p.removeprefix(".agent-state/outputs/")
    return p


class CheckResult:
    def __init__(self, check_id: str, title: str):
        self.check_id = check_id
        self.title = title
        self.status = "PASS"  # PASS / FAIL / WARN
        self.details: list[str] = []
        self.counts = ""

    def fail(self, msg: str):
        self.status = "FAIL"
        self.details.append(msg)

    def warn(self, msg: str):
        if self.status != "FAIL":
            self.status = "WARN"
        self.details.append(msg)

    def set_counts(self, text: str):
        self.counts = text


results: list[CheckResult] = []


def status_color(s: str) -> str:
    if s == "PASS":
        return GREEN
    elif s == "FAIL":
        return RED
    return YELLOW


# ============================================================
# EXTRACT AGENTS FROM TRANSITIONS (Source of Truth)
# ============================================================

# Non-agent top-level keys in transitions
TRANSITIONS_META_KEYS = {
    "version", "schema", "defaults", "rollback_rules", "entry",
}

# Keys that are quality gates or parallel groups (not regular agents)
GATE_KEYS_PREFIX = "gate_"
SPECIAL_TYPES = {"quality_gate", "parallel_group", "human_checkpoint", "decision_node"}


def get_all_transition_keys(trans: dict) -> list[str]:
    """All agent/gate/parallel keys from transitions."""
    return [k for k in trans if k not in TRANSITIONS_META_KEYS]


def get_regular_agents(trans: dict) -> list[str]:
    """Regular agents (not gates, not parallel groups)."""
    agents = []
    for k in get_all_transition_keys(trans):
        entry = trans[k]
        if isinstance(entry, dict):
            t = entry.get("type", "")
            if t not in SPECIAL_TYPES:
                agents.append(k)
        else:
            agents.append(k)
    return agents


def get_gates(trans: dict) -> list[str]:
    """Quality gate keys."""
    gates = []
    for k in get_all_transition_keys(trans):
        entry = trans[k]
        if isinstance(entry, dict) and entry.get("type") == "quality_gate":
            gates.append(k)
    return gates


def get_parallel_groups(trans: dict) -> list[str]:
    """Parallel group keys."""
    groups = []
    for k in get_all_transition_keys(trans):
        entry = trans[k]
        if isinstance(entry, dict) and entry.get("type") == "parallel_group":
            groups.append(k)
    return groups


def get_all_entities(trans: dict) -> list[str]:
    """All agents + gates + parallel groups."""
    return get_all_transition_keys(trans)


def get_division_agents(trans: dict, division: str) -> list[str]:
    """Get agents belonging to a specific division."""
    agents = []
    for k in get_all_transition_keys(trans):
        entry = trans[k]
        if isinstance(entry, dict) and entry.get("division") == division:
            agents.append(k)
    return agents


def extract_next_agents_recursive(obj, collected=None) -> set:
    """Recursively extract all next_agent values from a dict structure."""
    if collected is None:
        collected = set()
    if isinstance(obj, dict):
        for key, val in obj.items():
            if key == "next_agent" and isinstance(val, str):
                collected.add(val)
            elif key == "next" and isinstance(val, str):
                collected.add(val)
            elif key == "join_next" and isinstance(val, str):
                collected.add(val)
            elif key == "start_agent" and isinstance(val, str):
                collected.add(val)
            else:
                extract_next_agents_recursive(val, collected)
    elif isinstance(obj, list):
        for item in obj:
            extract_next_agents_recursive(item, collected)
    return collected


def extract_mutations_next_agent(obj) -> dict[str, set]:
    """Extract {event_key: set_of_current_agent_values} from mutations."""
    result = {}
    if not isinstance(obj, dict):
        return result
    for event_key, event_val in obj.items():
        if not isinstance(event_val, dict):
            continue
        set_block = event_val.get("set", {})
        if isinstance(set_block, dict) and "current_agent" in set_block:
            ca = set_block["current_agent"]
            if ca is not None:
                result[event_key] = ca
    return result


# ============================================================
# CHECK IMPLEMENTATIONS
# ============================================================

def check_1_1(trans: dict, mutations: dict):
    """transitions → state-mutations 에이전트 커버리지"""
    c = CheckResult("1.1", "transitions → state-mutations 에이전트 커버리지")
    all_keys = get_all_entities(trans)
    mut_keys = set(mutations.keys()) - {"version", "schema"}

    # Parallel group members don't need individual mutation entries
    parallel_members = set()
    for k in get_parallel_groups(trans):
        group = trans[k]
        if "agents" in group:
            parallel_members.update(group["agents"])

    missing = []
    for k in all_keys:
        if k not in mut_keys and k not in parallel_members:
            missing.append(k)

    if missing:
        for m in missing:
            if m in EXEMPT_AGENTS:
                c.warn(f"{m} (exempt) — mutations에 없음")
                continue
            entity = trans[m]
            etype = entity.get("type", "agent") if isinstance(entity, dict) else "agent"
            if etype in SPECIAL_TYPES and etype != "quality_gate":
                c.warn(f"{m} ({etype}) — mutations에 없음")
            else:
                c.fail(f"{m} — mutations에 없음")

    covered = len(all_keys) - len(missing)
    c.set_counts(f"{covered}/{len(all_keys)} entities covered")
    results.append(c)


def check_1_2(trans: dict, io_map: dict):
    """transitions → agent-io-map 에이전트 커버리지"""
    c = CheckResult("1.2", "transitions → agent-io-map 에이전트 커버리지")
    agents = get_regular_agents(trans)
    io_keys = set(io_map.keys()) - {"version", "schema", "output_base", "asset_base",
                                     "gate_outputs", "human_inputs", "all_output_files"}

    missing = []
    for a in agents:
        if a not in io_keys:
            missing.append(a)

    if missing:
        for m in missing:
            if m in EXEMPT_AGENTS:
                c.warn(f"{m} (exempt) — io-map에 없음")
            else:
                c.fail(f"{m} — io-map에 없음")

    covered = len(agents) - len(missing)
    c.set_counts(f"{covered}/{len(agents)} agents covered")
    results.append(c)


def check_1_3(trans: dict, prompt: dict):
    """transitions → prompt-assembly 에이전트 커버리지"""
    c = CheckResult("1.3", "transitions → prompt-assembly 에이전트 커버리지")
    agents = get_regular_agents(trans)
    prompt_keys = set(prompt.keys()) - {"version", "schema"}

    missing = []
    for a in agents:
        if a not in prompt_keys:
            missing.append(a)

    if missing:
        for m in missing:
            if m in EXEMPT_AGENTS:
                c.warn(f"{m} (exempt) — prompt-assembly에 없음")
            else:
                c.fail(f"{m} — prompt-assembly에 없음")

    covered = len(agents) - len(missing)
    c.set_counts(f"{covered}/{len(agents)} agents covered")
    results.append(c)


def check_1_4(trans: dict, checkpoints: dict):
    """human-checkpoints execution_map이 모든 에이전트 커버"""
    c = CheckResult("1.4", "human-checkpoints execution_map 커버리지")
    all_keys = get_all_entities(trans)
    exec_map = checkpoints.get("execution_map", {})

    # quick_builder and parallel groups/special nodes
    missing = []
    for k in all_keys:
        entry = trans[k]
        etype = entry.get("type", "") if isinstance(entry, dict) else ""
        if etype == "parallel_group":
            continue  # parallel groups don't need execution type
        if k not in exec_map:
            missing.append(k)

    if missing:
        for m in missing:
            if m in EXEMPT_AGENTS:
                c.warn(f"{m} (exempt) — execution_map에 없음")
            else:
                c.fail(f"{m} — execution_map에 없음")

    covered = len([k for k in all_keys
                   if k in exec_map or
                   (isinstance(trans[k], dict) and trans[k].get("type") == "parallel_group")])
    total = len([k for k in all_keys
                 if not (isinstance(trans[k], dict) and trans[k].get("type") == "parallel_group")])
    c.set_counts(f"{covered}/{total} entities covered")
    results.append(c)


def check_1_5(trans: dict, gates_auto: dict):
    """transitions의 모든 게이트가 quality-gates-auto에 존재"""
    c = CheckResult("1.5", "transitions 게이트 → quality-gates-auto 커버리지")
    t_gates = get_gates(trans)
    ga_keys = set(gates_auto.keys()) - {"version", "schema", "validation_defaults",
                                         "llm_validation_prompts"}

    # Also count user_validation_gate-like entries (gate_user_validation in gates-auto)
    missing = []
    for g in t_gates:
        if g not in ga_keys:
            missing.append(g)

    if missing:
        for m in missing:
            c.fail(f"{m} — quality-gates-auto에 없음")

    covered = len(t_gates) - len(missing)
    c.set_counts(f"{covered}/{len(t_gates)} gates covered")
    results.append(c)


def check_2_1(trans: dict, mutations: dict):
    """on_complete.next_agent (transitions) == on_complete.set.current_agent (mutations)"""
    c = CheckResult("2.1", "next_agent 라우팅 일치 (transitions vs mutations)")
    mismatches = []

    for k in get_all_entities(trans):
        entry = trans[k]
        if not isinstance(entry, dict):
            continue

        # Simple on_complete with next_agent
        on_complete = entry.get("on_complete", {})
        if isinstance(on_complete, dict) and "next_agent" in on_complete:
            t_next = on_complete["next_agent"]
            # Find corresponding in mutations
            mut_entry = mutations.get(k, {})
            mut_on_complete = mut_entry.get("on_complete", {})
            if isinstance(mut_on_complete, dict):
                mut_set = mut_on_complete.get("set", {})
                if isinstance(mut_set, dict) and "current_agent" in mut_set:
                    m_next = mut_set["current_agent"]
                    if t_next != m_next:
                        mismatches.append(
                            f"{k}: transitions=\"{t_next}\", mutations=\"{m_next}\""
                        )

        # on_pass for gates
        on_pass = entry.get("on_pass", {})
        if isinstance(on_pass, dict) and "next_agent" in on_pass:
            t_next = on_pass["next_agent"]
            mut_entry = mutations.get(k, {})
            # gates may use on_pass directly
            mut_on_pass = mut_entry.get("on_pass", {})
            if isinstance(mut_on_pass, dict):
                mut_set = mut_on_pass.get("set", {})
                if isinstance(mut_set, dict) and "current_agent" in mut_set:
                    m_next = mut_set["current_agent"]
                    if t_next != m_next:
                        mismatches.append(
                            f"{k}.on_pass: transitions=\"{t_next}\", mutations=\"{m_next}\""
                        )

        # on_fail for gates
        on_fail = entry.get("on_fail", {})
        if isinstance(on_fail, dict) and "next_agent" in on_fail:
            t_next = on_fail["next_agent"]
            mut_entry = mutations.get(k, {})
            mut_on_fail = mut_entry.get("on_fail", {})
            if isinstance(mut_on_fail, dict):
                mut_set = mut_on_fail.get("set", {})
                if isinstance(mut_set, dict) and "current_agent" in mut_set:
                    m_next = mut_set["current_agent"]
                    if t_next != m_next:
                        mismatches.append(
                            f"{k}.on_fail: transitions=\"{t_next}\", mutations=\"{m_next}\""
                        )

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_2_2(trans: dict, gates_auto: dict):
    """게이트 on_pass/on_fail 라우팅 일치 (transitions vs gates-auto)"""
    c = CheckResult("2.2", "게이트 라우팅 일치 (transitions vs quality-gates-auto)")
    mismatches = []

    ga_keys = set(gates_auto.keys()) - {"version", "schema", "validation_defaults",
                                         "llm_validation_prompts"}

    for g in get_gates(trans):
        t_entry = trans[g]
        ga_entry = gates_auto.get(g, {})
        if not ga_entry:
            continue

        # on_pass
        t_on_pass = t_entry.get("on_pass", {})
        ga_on_pass = ga_entry.get("on_pass", {})
        if isinstance(t_on_pass, dict) and isinstance(ga_on_pass, dict):
            t_next = t_on_pass.get("next_agent")
            ga_next = ga_on_pass.get("next_agent")
            # Handle branch case
            if t_next and ga_next and t_next != ga_next:
                mismatches.append(f"{g}.on_pass: transitions=\"{t_next}\", gates=\"{ga_next}\"")

        # on_fail
        t_on_fail = t_entry.get("on_fail", {})
        ga_on_fail = ga_entry.get("on_fail", {})
        if isinstance(t_on_fail, dict) and isinstance(ga_on_fail, dict):
            t_next = t_on_fail.get("next_agent")
            ga_next = ga_on_fail.get("next_agent")
            if t_next and ga_next and t_next != ga_next:
                mismatches.append(f"{g}.on_fail: transitions=\"{t_next}\", gates=\"{ga_next}\"")

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_2_3(trans: dict, parallel: dict):
    """parallel join_next 일치 (transitions vs parallel-groups)"""
    c = CheckResult("2.3", "parallel join_next 일치 (transitions vs parallel-groups)")
    mismatches = []

    for g in get_parallel_groups(trans):
        t_entry = trans[g]
        p_entry = parallel.get(g, {})
        if not p_entry:
            continue

        t_join_next = t_entry.get("join_next")
        p_join = p_entry.get("join", {})
        p_on_join = p_join.get("on_join", {}) if isinstance(p_join, dict) else {}
        p_join_next = p_on_join.get("next_agent") if isinstance(p_on_join, dict) else None

        if t_join_next and p_join_next and t_join_next != p_join_next:
            mismatches.append(
                f"{g}: transitions=\"{t_join_next}\", parallel=\"{p_join_next}\""
            )

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_3_1(trans: dict, io_map: dict):
    """output_file (transitions) == writes (io-map)"""
    c = CheckResult("3.1", "output_file 일치 (transitions vs io-map)")
    mismatches = []

    io_keys = set(io_map.keys()) - {"version", "schema", "output_base", "asset_base",
                                     "gate_outputs", "human_inputs", "all_output_files"}

    for a in io_keys:
        t_entry = trans.get(a, {})
        io_entry = io_map.get(a, {})

        if not isinstance(t_entry, dict) or not isinstance(io_entry, dict):
            continue

        # Get output from transitions
        t_output = t_entry.get("output_file", "")
        t_marker = t_entry.get("output_marker", "")
        t_out = normalize_path(t_output or t_marker)

        # Get writes from io-map
        writes = io_entry.get("writes", [])
        io_paths = set()
        for w in writes:
            if isinstance(w, dict):
                io_paths.add(normalize_path(w.get("path", "")))
            elif isinstance(w, str):
                io_paths.add(normalize_path(w))

        if t_out and io_paths and t_out not in io_paths:
            mismatches.append(f"{a}: transitions=\"{t_out}\", io-map={io_paths}")

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_3_2(trans: dict, io_map: dict):
    """must_read 파일이 어딘가에서 writes됨"""
    c = CheckResult("3.2", "must_read 파일이 writes로 존재")
    missing = []

    # Collect all written files
    all_writes = set()
    io_keys = set(io_map.keys()) - {"version", "schema", "output_base", "asset_base",
                                     "gate_outputs", "human_inputs", "all_output_files"}
    for a in io_keys:
        entry = io_map.get(a, {})
        if not isinstance(entry, dict):
            continue
        for w in entry.get("writes", []):
            if isinstance(w, dict):
                all_writes.add(normalize_path(w.get("path", "")))
            elif isinstance(w, str):
                all_writes.add(normalize_path(w))

    # Add gate auto-generated outputs
    gate_outputs = io_map.get("gate_outputs", {})
    for gk, gv in gate_outputs.items():
        if isinstance(gv, dict) and "auto_generates" in gv:
            all_writes.add(normalize_path(gv["auto_generates"]))

    # Add human inputs
    human_inputs = io_map.get("human_inputs", {})
    for hk in human_inputs:
        all_writes.add(normalize_path(hk))

    # Check must_read in transitions
    for k in get_all_entities(trans):
        entry = trans[k]
        if not isinstance(entry, dict):
            continue
        input_files = entry.get("input_files", {})
        if not isinstance(input_files, dict):
            continue
        must_read = input_files.get("must_read", [])
        if not isinstance(must_read, list):
            continue
        for mr in must_read:
            if isinstance(mr, str):
                norm = normalize_path(mr)
                if norm and norm not in all_writes and mr not in SYSTEM_FILES and norm not in SYSTEM_FILES:
                    missing.append(f"{k} must_read \"{norm}\" — 어디서도 writes 안 됨")

    if missing:
        for m in missing:
            c.warn(m)
    c.set_counts(f"{len(missing)} unmatched must_read files")
    results.append(c)


def check_3_3(trans: dict, prompt: dict):
    """prompt-assembly 파일 경로가 유효한 output 파일"""
    c = CheckResult("3.3", "prompt-assembly 파일 경로 유효성")
    invalid = []

    # Collect all known output filenames from transitions
    all_outputs = set()
    for k in get_all_entities(trans):
        entry = trans[k]
        if not isinstance(entry, dict):
            continue
        for field in ["output_file", "output_marker"]:
            val = entry.get(field, "")
            if val:
                all_outputs.add(normalize_path(val))

    # Also add special files
    all_outputs.add("project.json")

    prompt_keys = set(prompt.keys()) - {"version", "schema"}
    for pk in prompt_keys:
        entry = prompt[pk]
        if not isinstance(entry, dict):
            continue
        variables = entry.get("variables", {})
        if not isinstance(variables, dict):
            continue
        for vname, vdef in variables.items():
            if not isinstance(vdef, dict):
                continue
            path = vdef.get("path", "")
            if path:
                norm = normalize_path(path)
                if norm and norm not in all_outputs:
                    # Check fallback too
                    fallback = vdef.get("fallback", {})
                    if isinstance(fallback, dict):
                        fb_path = normalize_path(fallback.get("path", ""))
                        if fb_path and fb_path not in all_outputs:
                            invalid.append(f"{pk}.{vname}: \"{norm}\" not in outputs")
                    else:
                        invalid.append(f"{pk}.{vname}: \"{norm}\" not in outputs")

            # Check paths in file_list
            paths = vdef.get("paths", [])
            if isinstance(paths, list):
                for p in paths:
                    norm = normalize_path(p)
                    if norm and norm not in all_outputs:
                        invalid.append(f"{pk}.{vname}: \"{norm}\" not in outputs")

    if invalid:
        for i in invalid:
            c.warn(i)
    c.set_counts(f"{len(invalid)} unmatched paths")
    results.append(c)


def check_4_1(mutations: dict, persistence_text: str):
    """state-mutations의 iteration_count 키 == context-persistence 템플릿 키"""
    c = CheckResult("4.1", "iteration_count 키 일치 (mutations vs context-persistence)")

    # Extract iteration_count keys from mutations (increment blocks)
    mut_iter_keys = set()
    def find_increment_keys(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "increment" and isinstance(v, dict):
                    for ik in v:
                        # Handle dotted notation like "iteration_count.product_brief_revision"
                        clean = ik.removeprefix("iteration_count.")
                        mut_iter_keys.add(clean)
                else:
                    find_increment_keys(v)
        elif isinstance(obj, list):
            for item in obj:
                find_increment_keys(item)

    find_increment_keys(mutations)

    # Extract iteration_count keys from context-persistence.md
    pers_iter_keys = set()
    # Look for keys in the JSON template
    pattern = r'"iteration_count":\s*\{([^}]+)\}'
    match = re.search(pattern, persistence_text, re.DOTALL)
    if match:
        block = match.group(1)
        for key_match in re.finditer(r'"(\w+)"', block):
            pers_iter_keys.add(key_match.group(1))

    # Compare
    only_in_mut = mut_iter_keys - pers_iter_keys
    only_in_pers = pers_iter_keys - mut_iter_keys

    if only_in_mut:
        for k in sorted(only_in_mut):
            c.fail(f"\"{k}\" — mutations에만 있고 context-persistence에 없음")
    if only_in_pers:
        for k in sorted(only_in_pers):
            c.warn(f"\"{k}\" — context-persistence에만 있고 mutations에서 미사용")

    c.set_counts(f"mutations={len(mut_iter_keys)}, persistence={len(pers_iter_keys)}")
    results.append(c)


def check_4_2(gates_auto: dict, persistence_text: str):
    """quality-gates-auto retry_counter가 유효한 iteration_count 키"""
    c = CheckResult("4.2", "retry_counter 유효성 (gates-auto vs context-persistence)")

    # Extract iteration_count keys from persistence
    pers_iter_keys = set()
    pattern = r'"iteration_count":\s*\{([^}]+)\}'
    match = re.search(pattern, persistence_text, re.DOTALL)
    if match:
        block = match.group(1)
        for key_match in re.finditer(r'"(\w+)"', block):
            pers_iter_keys.add(key_match.group(1))

    # Find retry_counter references in gates-auto
    invalid = []
    def find_retry_counters(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "retry_counter" and isinstance(v, str):
                    clean = v.removeprefix("iteration_count.")
                    if clean not in pers_iter_keys:
                        invalid.append(f"{path}.{k}: \"{v}\" — 유효하지 않은 iteration_count 키")
                else:
                    find_retry_counters(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                find_retry_counters(item, f"{path}[{i}]")

    find_retry_counters(gates_auto)

    if invalid:
        for i in invalid:
            c.fail(i)
    c.set_counts(f"{len(invalid)} invalid retry_counters")
    results.append(c)


def check_5_1(trans: dict, parallel: dict):
    """멤버 리스트 일치 (transitions vs parallel-groups)"""
    c = CheckResult("5.1", "parallel 멤버 리스트 일치 (transitions vs parallel-groups)")
    mismatches = []

    for g in get_parallel_groups(trans):
        t_entry = trans[g]
        p_entry = parallel.get(g, {})
        if not p_entry:
            mismatches.append(f"{g} — parallel-groups에 없음")
            continue

        t_members = set(t_entry.get("agents", []))
        p_members_raw = p_entry.get("members", {})
        p_members = set(p_members_raw.keys()) if isinstance(p_members_raw, dict) else set()

        if t_members != p_members:
            only_t = t_members - p_members
            only_p = p_members - t_members
            if only_t:
                mismatches.append(f"{g}: transitions에만 있음: {only_t}")
            if only_p:
                mismatches.append(f"{g}: parallel-groups에만 있음: {only_p}")

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_5_2(trans: dict, parallel: dict):
    """parallel 멤버 이름이 유효한 에이전트"""
    c = CheckResult("5.2", "parallel 멤버가 유효한 에이전트")
    all_keys = set(get_all_entities(trans))
    invalid = []

    for g in parallel:
        if g in {"version", "schema"}:
            continue
        p_entry = parallel[g]
        if not isinstance(p_entry, dict):
            continue
        members = p_entry.get("members", {})
        if isinstance(members, dict):
            for m in members:
                if m not in all_keys:
                    invalid.append(f"{g}.{m} — transitions에 정의되지 않은 에이전트")

    if invalid:
        for i in invalid:
            c.fail(i)
    c.set_counts(f"{len(invalid)} invalid members")
    results.append(c)


def check_6_1(trans: dict):
    """Division별 에이전트 수 (CBO:5, CTO:7, CDO:6, CGO:8)"""
    c = CheckResult("6.1", "Division별 에이전트 수")
    mismatches = []

    for div, expected in DIVISION_COUNTS.items():
        agents = get_division_agents(trans, div)
        actual = len(agents)
        if actual != expected:
            mismatches.append(
                f"{div}: expected={expected}, actual={actual} ({agents})"
            )

    if mismatches:
        for m in mismatches:
            c.fail(m)

    # Show actual counts
    counts_str = ", ".join(
        f"{div}:{len(get_division_agents(trans, div))}"
        for div in DIVISION_COUNTS
    )
    c.set_counts(counts_str)
    results.append(c)


def check_6_2(trans: dict):
    """skippable_agents가 유효한 에이전트 이름"""
    c = CheckResult("6.2", "skippable_agents 유효성")
    all_keys = set(get_all_entities(trans))
    defaults = trans.get("defaults", {})
    skippable = defaults.get("skippable_agents", [])
    invalid = []

    for s in skippable:
        if s not in all_keys:
            invalid.append(f"\"{s}\" — transitions에 정의되지 않은 에이전트")

    if invalid:
        for i in invalid:
            c.fail(i)
    c.set_counts(f"{len(skippable)} skippable agents, {len(invalid)} invalid")
    results.append(c)


def check_6_3(io_map: dict, trans: dict):
    """all_output_files 리스트 완전성"""
    c = CheckResult("6.3", "all_output_files 리스트 완전성")

    listed = set(io_map.get("all_output_files", []))

    # Collect all actual writes from io-map agent entries
    actual_writes = set()
    io_keys = set(io_map.keys()) - {"version", "schema", "output_base", "asset_base",
                                     "gate_outputs", "human_inputs", "all_output_files"}
    for a in io_keys:
        entry = io_map.get(a, {})
        if not isinstance(entry, dict):
            continue
        for w in entry.get("writes", []):
            if isinstance(w, dict):
                actual_writes.add(normalize_path(w.get("path", "")))
            elif isinstance(w, str):
                actual_writes.add(normalize_path(w))

    # Add gate auto-generated
    gate_outputs = io_map.get("gate_outputs", {})
    for gk, gv in gate_outputs.items():
        if isinstance(gv, dict) and "auto_generates" in gv:
            actual_writes.add(normalize_path(gv["auto_generates"]))

    # Add human inputs
    human_inputs = io_map.get("human_inputs", {})
    for hk in human_inputs:
        actual_writes.add(normalize_path(hk))

    only_listed = listed - actual_writes
    only_actual = actual_writes - listed

    if only_actual:
        for f in sorted(only_actual):
            if f:  # skip empty
                c.fail(f"\"{f}\" — writes에 있지만 all_output_files에 없음")
    if only_listed:
        for f in sorted(only_listed):
            c.warn(f"\"{f}\" — all_output_files에 있지만 writes에서 발견 안 됨")

    c.set_counts(f"listed={len(listed)}, actual_writes={len(actual_writes)}")
    results.append(c)


def check_7_1(trans: dict):
    """agent id 필드 == YAML key"""
    c = CheckResult("7.1", "agent id 필드 == YAML key")
    mismatches = []

    for k in get_all_entities(trans):
        entry = trans[k]
        if not isinstance(entry, dict):
            continue
        agent_id = entry.get("id")
        if agent_id and agent_id != k:
            mismatches.append(f"key=\"{k}\", id=\"{agent_id}\"")

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


def check_7_2(trans: dict, checkpoints: dict):
    """execution 타입 일치 (transitions vs human-checkpoints)"""
    c = CheckResult("7.2", "execution 타입 일치 (transitions vs human-checkpoints)")
    mismatches = []

    exec_map = checkpoints.get("execution_map", {})

    for k in get_all_entities(trans):
        entry = trans[k]
        if not isinstance(entry, dict):
            continue
        t_exec = entry.get("execution")
        h_exec = exec_map.get(k)

        if t_exec and h_exec and t_exec != h_exec:
            mismatches.append(
                f"{k}: transitions=\"{t_exec}\", checkpoints=\"{h_exec}\""
            )

    if mismatches:
        for m in mismatches:
            c.fail(m)
    c.set_counts(f"{len(mismatches)} mismatches")
    results.append(c)


# ============================================================
# MAIN
# ============================================================

def main():
    # Load all files
    print(f"\n{BOLD}Loading files...{RESET}")
    data = {}
    for key, path in FILES.items():
        if not path.exists():
            print(f"  {RED}ERROR{RESET}: {path} not found")
            sys.exit(2)
        if key == "persistence":
            data[key] = load_text(path)
        else:
            data[key] = load_yaml(path)
        print(f"  OK: {path.name}")

    trans = data["transitions"]
    mutations = data["mutations"]
    gates_auto = data["gates"]
    parallel = data["parallel"]
    io_map = data["io_map"]
    prompt = data["prompt"]
    checkpoints = data["checkpoints"]
    persistence = data["persistence"]

    # Run all checks
    print(f"\n{'=' * 60}")
    print(f"{BOLD}Agent Company v5.1 — 정합성 검증 리포트{RESET}")
    print(f"{'=' * 60}\n")

    # Category 1: Agent Name Consistency
    print(f"{BOLD}[Category 1] Agent Name Consistency{RESET}")
    check_1_1(trans, mutations)
    check_1_2(trans, io_map)
    check_1_3(trans, prompt)
    check_1_4(trans, checkpoints)
    check_1_5(trans, gates_auto)

    # Category 2: Transition Route Consistency
    print(f"\n{BOLD}[Category 2] Transition Route Consistency{RESET}")
    check_2_1(trans, mutations)
    check_2_2(trans, gates_auto)
    check_2_3(trans, parallel)

    # Category 3: File Path Consistency
    print(f"\n{BOLD}[Category 3] File Path Consistency{RESET}")
    check_3_1(trans, io_map)
    check_3_2(trans, io_map)
    check_3_3(trans, prompt)

    # Category 4: Iteration Count Consistency
    print(f"\n{BOLD}[Category 4] Iteration Count Consistency{RESET}")
    check_4_1(mutations, persistence)
    check_4_2(gates_auto, persistence)

    # Category 5: Parallel Group Consistency
    print(f"\n{BOLD}[Category 5] Parallel Group Consistency{RESET}")
    check_5_1(trans, parallel)
    check_5_2(trans, parallel)

    # Category 6: Counts & Lists
    print(f"\n{BOLD}[Category 6] Counts & Lists{RESET}")
    check_6_1(trans)
    check_6_2(trans)
    check_6_3(io_map, trans)

    # Category 7: Internal Self-Consistency
    print(f"\n{BOLD}[Category 7] Internal Self-Consistency{RESET}")
    check_7_1(trans)
    check_7_2(trans, checkpoints)

    # Print results
    print(f"\n{'=' * 60}")
    print(f"{BOLD}상세 결과{RESET}")
    print(f"{'=' * 60}\n")

    for r in results:
        color = status_color(r.status)
        print(f"[{r.check_id}] {r.title}")
        print(f"  {color}{r.status}{RESET}  {r.counts}")
        for d in r.details:
            print(f"    - {d}")
        print()

    # Summary
    pass_count = sum(1 for r in results if r.status == "PASS")
    fail_count = sum(1 for r in results if r.status == "FAIL")
    warn_count = sum(1 for r in results if r.status == "WARN")

    print(f"{'=' * 60}")
    summary_parts = []
    summary_parts.append(f"{GREEN}{pass_count} PASS{RESET}")
    summary_parts.append(f"{RED}{fail_count} FAIL{RESET}")
    summary_parts.append(f"{YELLOW}{warn_count} WARN{RESET}")
    print(f"{BOLD}SUMMARY:{RESET} {' / '.join(summary_parts)}")
    print(f"{'=' * 60}\n")

    if fail_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
