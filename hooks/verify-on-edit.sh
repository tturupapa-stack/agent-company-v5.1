#!/bin/bash
# Hook: YAML 파일 수정 시 정합성 자동 검증
# PostToolUse(Edit|Write) → stdin으로 JSON 수신 → file_path 확인 → 검증 실행

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# ~/.claude/system/ 하위 YAML 파일인지 확인
SYSTEM_DIR="$HOME/.claude/system"
case "$FILE_PATH" in
  "$SYSTEM_DIR"/*.yaml|"$SYSTEM_DIR"/*.yml)
    ;;
  *)
    exit 0  # 대상 아님 — 통과
    ;;
esac

# 검증 실행
RESULT=$("$HOME/.claude/.venv/bin/python3" "$HOME/.claude/verify-consistency.py" 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 1 ]; then
  # FAIL 발견 — stderr로 피드백, exit 2로 블로킹
  echo "$RESULT" >&2
  echo "" >&2
  echo "정합성 검증 FAIL — 위 결과를 확인하고 수정하세요." >&2
  exit 2
fi

# PASS 또는 WARN — 통과
exit 0
