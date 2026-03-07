# Codex-Claude Loop 스킬 사용법

## 기본 사용 시나리오

### 1️⃣ 새로운 기능 개발

```
👤 사용자: "로그인 기능을 OAuth 2.0으로 구현해줘"

🤖 Claude:
[먼저 계획을 세움]
- OAuth 2.0 플로우 설계
- 보안 토큰 관리 방식
- 에러 핸들링 전략
...

[계획이 완성되면]
"이 계획을 Codex로 검증하겠습니다"
- 어떤 모델을 사용할까요? (gpt-5 / gpt-5-codex)
- Reasoning effort? (low / medium / high)

👤 사용자: "gpt-5-codex, high"

🤖 Claude:
[Codex에게 계획 검증 요청]
$ echo "Review this OAuth plan..." | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only

[Codex 피드백 요약]
"Codex가 2가지 이슈를 발견했습니다:
1. CSRF 토큰 검증 누락
2. Refresh token 로테이션 필요

계획을 수정하겠습니다..."

[계획 수정 후 재검증 또는 바로 구현]
👤 사용자: "구현해줘"

🤖 Claude:
[검증된 계획으로 구현 시작]
- Edit/Write 도구로 코드 작성
- 단계별로 구현
...

[구현 완료 후]
"구현이 완료되었습니다. Codex로 코드 리뷰를 받겠습니다"

$ echo "Review this implementation..." | codex exec --sandbox read-only

[Codex 리뷰 결과]
"Codex가 성능 개선 제안 1개를 발견했습니다. 적용하겠습니다..."
[수정 완료]
```

### 2️⃣ 코드 리뷰 & 개선

```
👤 사용자: "이 코드를 Codex-Claude loop으로 리뷰해줘"

🤖 Claude:
[먼저 코드 분석]
"몇 가지 개선점을 발견했습니다..."

[Codex로 검증]
$ echo "Review this code for bugs and performance..." | codex exec --sandbox read-only

[Codex 피드백 분석]
"Codex 발견:
- 잠재적 메모리 누수 1개
- 성능 최적화 2개
- 가독성 이슈 3개

수정을 진행하겠습니다"

👤 사용자: "응"

🤖 Claude:
[Edit/Write 도구로 코드 수정]
"수정 완료! 다시 Codex로 검증하겠습니다..."

$ echo "Verify the fixes..." | codex exec resume --last
```

### 3️⃣ 버그 수정

```
👤 사용자: "Claude가 만든 코드에 버그가 있어"

🤖 Claude:
"어떤 버그인지 확인했습니다.
수정하고 다시 Codex에게 검증받겠습니다"

[Claude가 수정]
[Edit/Write 도구로 코드 수정]

[Codex로 재검증]
$ echo "Verify this fix..." | codex exec resume --last

[Codex 검증 통과]
"수정 완료! Codex가 확인했습니다."
```

## 주요 명령어 패턴

### 1. 계획 검증 (Codex)
```bash
echo "Review this plan: [계획내용]" | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only
```

### 2. 구현 (Claude)
Claude가 Edit/Write/Read 등의 도구를 사용하여 직접 코드 작성

### 3. 코드 리뷰 (Codex)
```bash
echo "Review this implementation: [구현 설명]" | codex exec --sandbox read-only
```

### 4. 수정 적용 (Claude)
Claude가 Codex 피드백을 기반으로 코드 수정

### 5. 재검증 (Codex)
```bash
echo "Verify the fixes" | codex exec resume --last
```

## 언제 이 스킬을 쓰나?

✅ **이럴 때 사용:**
- 복잡한 기능 개발 (여러 단계 필요)
- 높은 품질이 중요한 코드
- 보안/성능이 critical한 작업
- 리팩토링 대규모 작업

❌ **이럴 땐 과함:**
- 간단한 일회성 수정
- 프로토타입/실험 코드
- 개인 학습용 간단한 예제

## 실전 팁

### 💡 Tip 1: 모델 선택
- **gpt-5**: 빠른 일반 작업
- **gpt-5-codex**: 복잡한 코드 분석 (권장)

### 💡 Tip 2: Reasoning Effort
- **low**: 간단한 검증
- **medium**: 일반적인 작업 (권장)
- **high**: critical한 로직, 보안 관련

### 💡 Tip 3: 역할 분담
```
Claude: 모든 코드 작성 및 수정
Codex: 모든 검증 및 리뷰
```

### 💡 Tip 4: 반복 주기
```
구현 → 리뷰 → 수정 → 재검증
작은 변경: 1회 리뷰
중간 변경: 2-3회 반복
큰 변경: 완전 검증까지 반복
```

## 실제 워크플로우 예시

```
1. 👤 "결제 시스템 만들어줘"

2. 🤖 Claude가 계획 수립
   - Stripe API 통합
   - 웹훅 처리
   - 환불 로직

3. 🤖 Codex로 계획 검증
   $ codex exec ... --sandbox read-only

4. 📝 피드백: "웹훅 서명 검증 추가 필요"

5. 🤖 Claude가 계획 수정

6. ✅ 재검증 통과

7. 🔨 Claude가 구현
   Edit/Write 도구로 코드 작성

8. 👀 Codex가 코드 리뷰
   $ codex exec ... --sandbox read-only
   "성능 이슈 1개, 보안 개선 2개"

9. 🔧 Claude가 피드백 반영
   Edit 도구로 코드 수정

10. ✅ Codex 재검증
    $ codex exec resume --last
    "모든 이슈 해결됨!"

11. ✅ 완료!
```

핵심은 **"계획 → 검증 → 구현 → 리뷰 → 수정 → 재검증"** 루프입니다! 🔄