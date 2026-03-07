# Codex-Claude-Cursor Loop 스킬 사용법

## 3-Way 순차 검증 워크플로우

이 스킬은 **세 가지 AI를 순차적으로 활용**하여 최고 품질의 코드를 만듭니다:
- **Claude**: 계획 수립 + 최종 검토
- **Codex**: 계획 검증 + 코드 리뷰
- **Cursor**: 코드 구현

## 기본 사용 시나리오

### 1️⃣ 새로운 기능 개발

```
👤 사용자: "로그인 기능을 OAuth 2.0으로 구현해줘"

🤖 Claude:
[1단계: 계획 수립]
- OAuth 2.0 플로우 설계
- 보안 토큰 관리 방식
- 에러 핸들링 전략
...

[2단계: Codex로 계획 검증]
"Codex로 계획을 검증하겠습니다"
- 어떤 모델을 사용할까요? (gpt-5 / gpt-5-codex)
- Reasoning effort? (low / medium / high)

👤 사용자: "gpt-5-codex, high"

🤖 Claude:
$ echo "Review this OAuth plan..." | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only

[Codex 피드백]
"Codex가 2가지 이슈를 발견했습니다:
1. CSRF 토큰 검증 누락
2. Refresh token 로테이션 필요"

[계획 수정 후 재검증]
"계획을 수정했습니다. Codex 재검증 통과!"

[3단계: Cursor 세션 설정 및 구현]
"이제 Cursor에게 구현을 맡기겠습니다"
- 새 세션을 시작할까요, 아니면 이전 세션을 이어서 할까요?

👤 사용자: "새 세션"

🤖 Claude:
- 어떤 Cursor 모델을 사용할까요? (composer-1 / claude-3.5-sonnet / gpt-4o)

👤 사용자: "claude-3.5-sonnet"

🤖 Claude:
$ cursor-agent --model "claude-3.5-sonnet" -p --force "Implement this OAuth plan..."

[Cursor가 구현 완료]
[세션 ID 저장: session-abc-123]

[4단계: Codex 코드 리뷰]
$ echo "Review this implementation..." | codex exec --sandbox read-only

"Codex가 성능 이슈 1개를 발견했습니다"

[5단계: Claude 최종 검토]
[Read 도구로 코드 확인]
"추가로 보안 개선 1개가 필요합니다"

[6단계: 수정]
[Claude가 수정 계획 작성]
$ cursor-agent --resume="session-abc-123" -p --force "Fix these issues..."

[Cursor가 같은 세션에서 수정 - 이전 컨텍스트 유지!]

[7단계: 재검증]
$ echo "Verify fixes..." | codex exec --sandbox read-only
[Claude 최종 확인]

✅ "모든 검증 통과! 완료되었습니다"
```

### 2️⃣ 코드 리뷰 & 개선

```
👤 사용자: "이 코드를 3-way loop으로 리뷰해줘"

🤖 Claude:
[1단계: Claude가 코드 분석 및 개선 계획]
"개선 계획을 수립했습니다"

[2단계: Codex로 계획 검증]
$ echo "Review this improvement plan..." | codex exec --sandbox read-only

"Codex 승인!"

[3단계: Cursor 세션 설정 및 개선 구현]
- 새 세션으로 시작할까요?

👤 사용자: "응"

🤖 Claude:
$ cursor-agent --model "composer-1" -p --force "Implement improvements..."
[세션 ID: session-improve-456]

[4단계: Codex 코드 리뷰]
$ echo "Review the improved code..." | codex exec --sandbox read-only

"Codex 발견:
- 잠재적 메모리 누수 1개
- 성능 최적화 2개"

[5단계: Claude 최종 검토]
"Codex가 맞습니다. 추가 수정이 필요합니다"

[6단계: 재수정 - 같은 세션]
$ cursor-agent --resume="session-improve-456" -p --force "Fix these issues..."

[7단계: 재검증]
$ echo "Verify fixes..." | codex exec --sandbox read-only
[Claude 확인]

✅ "완벽합니다!"
```

### 3️⃣ 버그 수정 (기존 세션 이어서)

```
👤 사용자: "아까 만든 코드에 버그가 있어"

🤖 Claude:
"기존 Cursor 세션을 이어서 할까요?"

👤 사용자: "응, 아까 그 세션"

🤖 Claude:
$ cursor-agent ls
[session-abc-123: OAuth 구현]

[1단계: Claude가 버그 분석 및 수정 계획]
"버그를 확인했습니다. 수정 계획을 수립합니다"

[2단계: Codex로 수정 계획 검증]
$ echo "Review this bug fix plan..." | codex exec --sandbox read-only

"Codex: 계획이 적절합니다"

[3단계: Cursor가 같은 세션에서 수정]
$ cursor-agent --resume="session-abc-123" -p --force "Fix this bug..."

[4단계: Codex가 수정 검증]
$ echo "Verify the bug fix..." | codex exec --sandbox read-only

"Codex: 버그가 제대로 수정되었습니다"

[5단계: Claude 최종 확인]
[Read 도구로 코드 확인]

✅ "버그 수정 완료!"
```

## 주요 명령어 패턴

### 1. 계획 작성 (Claude)
Claude가 TodoWrite, Read 등의 도구를 사용하여 상세한 계획 작성

### 2. 계획 검증 (Codex)
```bash
echo "Review this plan: [계획내용]" | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only
```

### 3. 계획 수정 (Claude)
Claude가 Codex 피드백을 반영하여 계획 수정

### 4. 구현 (Cursor)
```bash
cursor-agent --model "claude-3.5-sonnet" -p --force "Implement this plan: [검증된 계획]"
```

### 5. 코드 리뷰 (Codex)
```bash
echo "Review this implementation for bugs and performance: [구현 설명]" | codex exec --sandbox read-only
```

### 6. 최종 검토 (Claude)
Claude가 Read 도구를 사용하여 Codex 리뷰 + 코드 최종 검토

### 7. 수정 계획 작성 (Claude)
Claude가 Codex + Claude의 발견 사항을 종합하여 수정 계획 작성

### 8. 수정 적용 (Cursor - 같은 세션)
```bash
# IMPORTANT: 같은 세션 ID 사용으로 컨텍스트 유지
cursor-agent --resume="<session-id>" -p --force "Fix these issues: [수정 계획]"
```

### 9. 재검증 (Codex + Claude)
5-6단계 반복하여 모든 이슈 해결까지 검증

## 언제 이 스킬을 쓰나?

✅ **이럴 때 사용:**
- 복잡한 기능 개발 (여러 단계 필요)
- **최고 품질이 중요한 코드** (3중 검증)
- **보안/성능이 critical한 작업** (Codex가 2번 검증)
- 리팩토링 대규모 작업
- Claude의 계획 + Codex의 검증 + Cursor의 코딩 능력을 모두 활용

❌ **이럴 땐 과함:**
- 간단한 일회성 수정
- 프로토타입/실험 코드
- 개인 학습용 간단한 예제
- 빠른 반복이 필요한 MVP

## 실전 팁

### 💡 Tip 1: 모델 선택
**Codex:**
- **gpt-5-codex**: 복잡한 로직 검증 (권장)
- **gpt-5**: 빠른 검증
- **Reasoning effort**: critical한 작업은 `high` 사용

**Cursor:**
- **composer-1**: Cursor 전용 모델 (권장)
- **claude-3.5-sonnet**: 복잡한 코드 구현
- **gpt-4o**: 빠른 구현

**중요:** 프로젝트 전체에서 동일한 모델 조합 사용 권장

### 💡 Tip 2: 3-Way 역할 분담
```
Claude: 계획 수립 + 최종 아키텍처 검토
Codex: 계획 검증 (로직/보안) + 코드 리뷰 (버그/성능)
Cursor: 모든 코드 작성 및 수정
```

### 💡 Tip 3: 반복 주기
```
계획(Claude) → 검증(Codex) → 구현(Cursor) →
리뷰(Codex) → 최종검토(Claude) → 수정(Cursor) → 재검증

작은 변경: 1회 루프
중간 변경: 2-3회 반복
큰 변경: 완전 검증까지 반복
```

### 💡 Tip 4: 검증 포인트
- **Codex 계획 검증**: 로직 오류, 엣지 케이스, 보안 취약점
- **Codex 코드 리뷰**: 버그, 성능 이슈, 베스트 프랙티스
- **Claude 최종 검토**: 아키텍처 일관성, 전체적인 품질

### 💡 Tip 5: 세션 관리
- **새 기능 시작**: 새 세션으로 시작
- **반복 수정**: 같은 세션 ID로 계속 진행
- **이전 작업 재개**: `cursor-agent ls`로 목록 확인 후 `--resume` 사용
- **세션 ID 저장**: 첫 실행 후 세션 ID를 기록하고 재사용

### 💡 Tip 6: 효율성
- Codex는 read-only sandbox 사용 (빠른 검증)
- Claude는 필요한 파일만 Read
- 각 단계별 피드백을 명확히 문서화
- Cursor 세션 유지로 컨텍스트 손실 방지

## 실제 워크플로우 예시

```
1. 👤 "결제 시스템 만들어줘"

2. 🤖 Claude가 계획 수립
   - Stripe API 통합
   - 웹훅 처리
   - 환불 로직

3. 🔍 Codex로 계획 검증
   $ echo "Review plan..." | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only

4. 📝 Codex 피드백: "웹훅 서명 검증 추가 필요"

5. 🤖 Claude가 계획 수정
   - 웹훅 서명 검증 로직 추가

6. 🔍 Codex 재검증 통과!

7. 🔨 Cursor가 구현
   $ cursor-agent --model "composer" -p --force "Implement this plan..."
   [Cursor가 코드 작성 완료]

8. 🔍 Codex가 코드 리뷰
   $ echo "Review implementation..." | codex exec --sandbox read-only
   "성능 이슈 1개, 보안 개선 2개 발견"

9. 👀 Claude 최종 검토
   Read 도구로 코드 분석
   "Codex가 맞음. 추가로 로깅 개선 필요"

10. 🔧 Claude가 수정 계획 작성
    Codex + Claude 피드백 종합

11. ✅ Cursor가 수정 적용 (같은 세션)
    $ cursor-agent --resume="session-xyz" -p --force "Fix these issues..."

12. 🔍 Codex 재검증
    $ echo "Verify fixes..." | codex exec --sandbox read-only
    "모든 이슈 해결!"

13. 👀 Claude 최종 확인
    "완벽합니다!"

14. ✅ 완료!
```

핵심은 **"계획(Claude) → 검증(Codex) → 구현(Cursor) → 리뷰(Codex) → 최종검토(Claude) → 수정(Cursor) → 재검증(Codex+Claude)"** 루프입니다! 🔄

## 3-Way Loop의 장점

✨ **삼중 품질 보증:**
1. **Codex 계획 검증**: 설계 단계에서 문제 사전 차단
2. **Codex 코드 리뷰**: 구현의 버그와 성능 이슈 포착
3. **Claude 최종 검토**: 아키텍처와 전체 품질 확인

🎯 **각자의 강점 활용:**
- Claude: 전략적 사고, 아키텍처 설계
- Codex: 깊은 코드 분석, 버그 탐지
- Cursor: 빠르고 정확한 구현 (세션 유지로 컨텍스트 보존)

## 이전 세션 재개 예시

```
👤 사용자: "어제 작업하던 OAuth 구현 이어서 해줘"

🤖 Claude:
"이전 Cursor 세션을 찾아보겠습니다"

$ cursor-agent ls

세션 목록:
- session-abc-123: OAuth 2.0 구현 (2일 전)
- session-xyz-789: 결제 시스템 (1주일 전)

👤 사용자: "session-abc-123으로 이어서"

🤖 Claude:
[계획 수립]
"이전 작업 확인:
- OAuth login 구현 완료
- Token refresh 구현 완료

이어서 할 작업:
- Logout 기능 추가
- Session 만료 처리"

[Codex 계획 검증]
$ echo "Review plan..." | codex exec --sandbox read-only

[Cursor로 이어서 구현]
$ cursor-agent --resume="session-abc-123" -p --force "Continue implementation..."

✅ "이전 컨텍스트를 유지하며 작업 완료!"
```