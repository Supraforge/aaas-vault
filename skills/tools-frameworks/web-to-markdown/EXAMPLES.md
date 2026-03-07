# 실전 예제 모음

다양한 상황에서 Web to Markdown 스킬을 활용하는 방법을 소개합니다.

## 1. 개발 문서 아카이빙

### 시나리오
프로젝트에서 사용하는 라이브러리들의 공식 문서를 로컬에 백업하고 싶습니다.

### 실행
```
You: 이 문서들을 project-docs 폴더에 저장해줘
- https://react.dev/reference/react
- https://redux.js.org/introduction/getting-started
- https://tanstack.com/query/latest/docs/react/overview

Claude: project-docs 폴더를 생성하고 3개의 문서를 변환하겠습니다.

[변환 중...]

✅ 완료!
project-docs/
├── react-reference.md
├── redux-getting-started.md
└── tanstack-query-overview.md

총 3개 파일, 약 45KB
```

### 결과
오프라인에서도 문서를 참고할 수 있고, 버전 관리 시스템에 포함시켜 팀과 공유 가능합니다.

---

## 2. 블로그 글 수집

### 시나리오
좋은 기술 블로그 글들을 발견할 때마다 나중에 다시 읽기 위해 저장하고 싶습니다.

### 실행
```
You: https://blog.example.com/great-article 이 블로그 글을 reading-list 폴더에 저장해줘

Claude: 파일명은 어떻게 할까요? 또는 자동으로 생성할까요?

You: 제목 기반으로 자동 생성해줘

Claude: ✅ 저장 완료!
📄 reading-list/understanding-react-hooks.md
📊 약 3,250 단어

제목: "Understanding React Hooks: A Deep Dive"
작성자: John Doe
```

### 심화: 태그 추가
```
You: 이 글에 프론트매터로 태그 추가해줘

Claude: [파일에 프론트매터 추가]

---
title: Understanding React Hooks: A Deep Dive
author: John Doe
url: https://blog.example.com/great-article
saved_date: 2024-01-15
tags:
  - react
  - hooks
  - frontend
---

[본문...]
```

---

## 3. 튜토리얼 시리즈 다운로드

### 시나리오
온라인 강좌의 모든 레슨을 순서대로 저장하고 싶습니다.

### 실행
```
You: 이 튜토리얼 시리즈를 전부 저장해줘. 순서대로 번호를 붙여서
- https://tutorial.com/lesson-intro
- https://tutorial.com/lesson-basics
- https://tutorial.com/lesson-advanced
- https://tutorial.com/lesson-conclusion

Claude: tutorials/web-dev-course/ 폴더에 저장하겠습니다.

✅ 완료!
tutorials/web-dev-course/
├── 01-intro.md
├── 02-basics.md
├── 03-advanced.md
└── 04-conclusion.md
```

### 추가 요청
```
You: 전체 목차를 만들어줘

Claude: [index.md 파일 생성]

# Web Development Course

## 목차

1. [Introduction](01-intro.md)
2. [Basics](02-basics.md)
3. [Advanced Topics](03-advanced.md)
4. [Conclusion](04-conclusion.md)

---
전체 약 15,000 단어
예상 학습 시간: 2-3시간
```

---

## 4. 뉴스 아티클 아카이브

### 시나리오
중요한 뉴스 기사를 날짜별로 아카이빙하고 싶습니다.

### 실행
```
You: 오늘자 중요한 기사들을 archive/2024/01/ 폴더에 저장해줘
- https://news.com/tech-breakthrough
- https://news.com/market-update
- https://news.com/policy-change

Claude: ✅ 저장 완료!
archive/2024/01/
├── 2024-01-15-tech-breakthrough.md
├── 2024-01-15-market-update.md
└── 2024-01-15-policy-change.md

날짜가 파일명에 자동으로 포함되었습니다.
```

---

## 5. API 문서 로컬 복사

### 시나리오
자주 참고하는 API 문서를 로컬에 두고 빠르게 검색하고 싶습니다.

### 실행
```
You: Stripe API 문서의 주요 섹션들을 api-docs/stripe/ 폴더에 저장해줘
- https://stripe.com/docs/api/authentication
- https://stripe.com/docs/api/charges
- https://stripe.com/docs/api/customers
- https://stripe.com/docs/api/subscriptions

Claude: ✅ 완료!
api-docs/stripe/
├── authentication.md
├── charges.md
├── customers.md
└── subscriptions.md
```

### 검색 활용
```
You: customers.md 파일에서 "create customer" 예제 찾아줘

Claude: [파일 검색 및 관련 섹션 표시]

## Create a Customer

```javascript
const customer = await stripe.customers.create({
  email: 'customer@example.com',
  source: 'tok_visa',
});
```
```

---

## 6. GitHub README 수집

### 시나리오
유용한 오픈소스 프로젝트들의 README를 모아서 영감을 얻고 싶습니다.

### 실행
```
You: 이 프로젝트들의 README를 awesome-readmes 폴더에 저장해줘
- https://github.com/facebook/react
- https://github.com/vercel/next.js
- https://github.com/tailwindlabs/tailwindcss

Claude: ✅ 완료!
awesome-readmes/
├── react-README.md
├── nextjs-README.md
└── tailwindcss-README.md
```

---

## 7. 레시피 웹사이트 저장

### 시나리오
좋아하는 요리 레시피를 마크다운으로 저장하여 개인 레시피북을 만들고 싶습니다.

### 실행
```
You: 이 레시피를 recipes/italian/ 폴더에 저장해줘
https://cooking.com/classic-carbonara

Claude: ✅ 저장 완료!

📄 recipes/italian/classic-carbonara.md

# Classic Carbonara

## 재료
- 스파게티 400g
- 판체타 200g
- 달걀 4개
- 파마산 치즈 100g
[...]

## 조리법
1. 물을 끓이고...
[...]
```

---

## 8. 학술 논문 요약본

### 시나리오
arXiv 논문의 요약본을 저장하고 싶습니다.

### 실행
```
You: https://arxiv.org/abs/2301.12345 이 논문의 요약과 주요 내용만 추출해서 저장해줘

Claude: 논문의 abstract와 주요 섹션을 추출하겠습니다.

✅ 저장 완료!
papers/transformers-survey.md

제목: "A Survey of Transformer Architectures"
저자: Smith et al.
발행일: 2023-01-15

주요 내용:
- Abstract
- Introduction
- Key Contributions
- Conclusion
```

---

## 9. 제품 문서 번역 준비

### 시나리오
영문 제품 문서를 번역하기 위해 먼저 마크다운으로 변환하고 싶습니다.

### 실행
```
You: https://product.com/docs/user-guide 이걸 마크다운으로 저장하고, 한국어로 번역 준비해줘

Claude: 먼저 마크다운으로 변환하겠습니다.

✅ user-guide.md 저장 완료!

번역 작업을 시작할까요?

You: 네, user-guide-ko.md로 번역해줘

Claude: [번역 진행...]
✅ user-guide-ko.md 생성 완료!
```

---

## 10. 웹 포트폴리오 아카이빙

### 시나리오
영감을 주는 포트폴리오 사이트들의 "About" 페이지를 모으고 싶습니다.

### 실행
```
You: 이 디자이너들의 About 페이지를 inspiration/portfolios/ 폴더에 저장해줘
- https://designer1.com/about
- https://designer2.com/about
- https://designer3.com/about

Claude: ✅ 완료!
inspiration/portfolios/
├── designer1-about.md
├── designer2-about.md
└── designer3-about.md

각 파일에는 자기소개, 경력, 작업 철학이 포함되어 있습니다.
```

---

## 11. AI 최적화 모드 - 기술 문서

### 시나리오
기술 문서를 AI 에이전트가 컨텍스트로 활용할 수 있도록 최적화하여 저장하고 싶습니다.

### 실행
```
You: https://react.dev/reference/react/useState 를 AI가 읽기 좋게 변환해줘

Claude: AI 최적화 모드로 변환하겠습니다.
구조화된 프론트매터와 명확한 섹션을 추가합니다.

✅ 저장 완료!
📄 docs/react-useState.context.md
📊 원본 3,500 토큰 → 최적화 2,100 토큰 (40% 절감)
```

### 결과 미리보기
```markdown
---
title: "useState - React Reference"
url: "https://react.dev/reference/react/useState"
author: "React Team"
date: "2024-01-15"
word_count: 1800
topics: ["React", "Hooks", "State Management", "Frontend"]
summary: |
  useState는 컴포넌트에 상태 변수를 추가할 수 있는 React Hook입니다.
  초기 상태를 인자로 받아 현재 상태와 setter 함수를 반환합니다.
main_points:
  - 상태 변수와 setter 함수를 배열로 반환
  - 초기 상태는 함수로도 전달 가능
  - 상태 업데이트는 다음 렌더링에 반영
  - 객체/배열 상태는 불변성 유지 필요
content_type: "documentation"
difficulty: "beginner"
---

# useState - React Reference

## 핵심 요약

useState는 함수형 컴포넌트에 상태를 추가하는 Hook입니다.
초기값을 받아 [상태, setter] 배열을 반환하며, setter 호출 시 리렌더링을 트리거합니다.

## 주요 내용

### 기본 사용법

**Syntax**:
```javascript
const [state, setState] = useState(initialState);
```

**Parameters**:
- `initialState`: 초기 상태값 (any type)

**Returns**: `[state, setState]`
- `state`: 현재 상태
- `setState`: 상태 업데이트 함수

### 상태 업데이트

**직접 업데이트**:
```javascript
setState(newValue);
```

**함수형 업데이트**:
```javascript
setState(prev => prev + 1);
```

## 핵심 인사이트

- **초기화는 한 번만**: 초기 상태는 첫 렌더링에서만 사용
- **비동기 업데이트**: setState는 즉시 반영되지 않음
- **불변성 유지**: 객체/배열은 새로운 참조로 업데이트
- **함수형 업데이트**: 이전 상태 기반 업데이트 시 필수

## 실용적 적용

**카운터 예제**:
```javascript
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

**입력 폼**:
```javascript
function Form() {
  const [text, setText] = useState('');
  return <input value={text} onChange={e => setText(e.target.value)} />;
}
```

## 결론

useState는 React의 가장 기본적이면서 중요한 Hook입니다.
상태 관리의 기초를 이해하면 더 복잡한 Hooks도 쉽게 활용할 수 있습니다.
```

---

## 12. AI 최적화 모드 - 블로그 아티클

### 시나리오
기술 블로그 글을 AI가 학습하기 좋은 형태로 변환하고 싶습니다.

### 실행
```
You: https://blog.example.com/microservices-best-practices 를 컨텍스트로 사용하기 좋게 변환해줘

Claude: AI 최적화 모드로 변환하겠습니다.

✅ 저장 완료!
📄 knowledge-base/microservices-best-practices.context.md
📊 원본 4,200 토큰 → 최적화 2,500 토큰 (40% 절감)

프론트매터에 주제, 핵심 포인트, 난이도가 포함되어 있어
AI가 빠르게 문서의 맥락을 파악할 수 있습니다.
```

### 결과 특징
- **프론트매터**: 주제, 저자, 핵심 요약 포함
- **구조화**: 명확한 섹션 구분 (H2/H3)
- **인사이트 추출**: 저자의 주요 주장과 근거 정리
- **실용적 조언**: 즉시 적용 가능한 팁 강조
- **노이즈 제거**: 광고, 댓글, 네비게이션 완전 제거

---

## 13. AI 최적화 모드 - 여러 문서 일괄 처리

### 시나리오
여러 기술 문서를 AI 최적화 모드로 일괄 변환하여 지식 베이스를 구축하고 싶습니다.

### 실행
```
You: 이 문서들을 AI 학습용으로 변환해서 knowledge-base/react/ 폴더에 저장해줘
- https://react.dev/reference/react/useState
- https://react.dev/reference/react/useEffect
- https://react.dev/reference/react/useContext
- https://react.dev/reference/react/useReducer
- https://react.dev/reference/react/useMemo

Claude: 5개 문서를 AI 최적화 모드로 변환하겠습니다.

[변환 중...]

✅ 완료!
knowledge-base/react/
├── useState.context.md
├── useEffect.context.md
├── useContext.context.md
├── useReducer.context.md
└── useMemo.context.md

총 5개 파일
원본: 약 18,000 토큰
최적화: 약 10,500 토큰 (42% 절감)

각 파일에는:
- 구조화된 프론트매터
- 핵심 요약 (3-5줄)
- 명확한 API 레퍼런스
- 실전 예제
- 주요 인사이트
```

### 활용 방법
```
User: useState와 useReducer의 차이점을 알려줘

AI Agent:
[knowledge-base/react/useState.context.md 읽기]
[knowledge-base/react/useReducer.context.md 읽기]

프론트매터를 통해 빠르게 각 Hook의 용도를 파악했습니다:
- useState: 단순 상태 관리
- useReducer: 복잡한 상태 로직

주요 차이점:
1. [구조화된 문서에서 추출한 정확한 정보]
2. [...]
```

---

## 14. AI 최적화 모드 - RAG 시스템 구축

### 시나리오
AI 에이전트가 참고할 수 있는 RAG (Retrieval-Augmented Generation) 시스템을 구축하고 싶습니다.

### 실행
```
You: 우리 프로젝트 관련 문서들을 AI 최적화 모드로 변환해줘
- 내부 API 문서 20개
- 기술 블로그 15개
- 공식 라이브러리 문서 10개

Claude: 총 45개 문서를 AI 최적화 모드로 변환하겠습니다.

[변환 진행...]

✅ 완료!
rag-knowledge-base/
├── api-docs/ (20 files)
├── blog-posts/ (15 files)
└── library-docs/ (10 files)

모든 파일은 .context.md 확장자로 저장되었으며,
프론트매터의 topics 필드로 자동 분류 가능합니다.
```

### 시스템 구조
```
1. 문서 변환 (AI 최적화 모드)
   ↓
2. 프론트매터에서 topics 추출
   ↓
3. 벡터 데이터베이스에 인덱싱
   ↓
4. 사용자 질문 시 관련 문서 검색
   ↓
5. 구조화된 섹션에서 정확한 정보 추출
   ↓
6. AI 에이전트가 답변 생성
```

### 장점
- **빠른 검색**: 프론트매터의 topics로 즉시 필터링
- **정확한 추출**: 명확한 H2/H3 구조로 특정 정보 찾기 쉬움
- **토큰 절감**: 필요한 섹션만 컨텍스트에 포함
- **일관성**: 모든 문서가 동일한 구조로 통일

---

## 15. AI 최적화 모드 - 비교 분석

### 시나리오
두 가지 기술이나 접근법을 비교 분석하기 위해 문서를 최적화하여 저장합니다.

### 실행
```
You: React와 Vue의 상태 관리를 비교하고 싶어. 관련 문서들을 AI 최적화 모드로 변환해줘
- https://react.dev/learn/managing-state
- https://vuejs.org/guide/essentials/reactivity-fundamentals.html

Claude: 2개 문서를 AI 최적화 모드로 변환하겠습니다.

✅ 완료!
comparisons/state-management/
├── react-state.context.md
└── vue-reactivity.context.md

이제 AI가 두 문서의 프론트매터와 핵심 요약을 읽고
빠르게 차이점을 분석할 수 있습니다.
```

### AI 분석 예시
```
AI Agent가 두 .context.md 파일을 읽고:

1. 프론트매터에서 주제 확인:
   - React: ["state", "hooks", "immutability"]
   - Vue: ["reactivity", "ref", "reactive"]

2. 핵심 요약 비교:
   - React: 불변성 기반, 명시적 상태 업데이트
   - Vue: 반응성 시스템, 자동 추적

3. 핵심 인사이트 추출:
   - React: "상태는 불변 객체로 관리"
   - Vue: "ref/reactive로 반응성 자동 생성"

4. 비교 결과 생성:
   [상세한 비교 분석...]
```

---

## 16. 듀얼 모드 - 원본 + AI 최적화 동시 생성 ⭐⭐

### 시나리오
웹페이지를 사람이 읽을 원본과 AI가 활용할 최적화 버전 모두 필요합니다.

### 실행
```
You: https://react.dev/reference/react/useState 원본이랑 AI 최적화 버전 둘 다 만들어줘

Claude: 듀얼 모드로 변환하겠습니다.

[1단계: 원본 마크다운 변환 중...]
✅ useState.md 생성 완료

[2단계: AI 최적화 버전 변환 중...]
✅ useState.context.md 생성 완료

✅ 듀얼 모드 변환 완료! 2개 파일이 생성되었습니다.

📄 원본 마크다운:
- 파일: useState.md
- 크기: 약 3,500 글자
- 용도: 사람이 읽기 좋은 원본 보존
- 특징: 모든 내용 포함, 원본 구조 유지

[View file](computer:///path/to/useState.md)

📄 AI 최적화 버전:
- 파일: useState.context.md
- 크기: 약 2,100 글자 (40% 절감)
- 용도: AI 컨텍스트로 활용
- 특징: 구조화된 프론트매터, 핵심 요약, 명확한 섹션

[View file](computer:///path/to/useState.context.md)

💡 팁:
- 원본(.md)은 사람이 읽을 때 사용
- AI 최적화(.context.md)는 RAG 시스템이나 AI 에이전트 컨텍스트로 사용
```

### 파일 비교

#### useState.md (원본)
```markdown
# useState

useState is a React Hook that lets you add a state variable to your component.

```jsx
const [state, setState] = useState(initialState)
```

## Reference

### useState(initialState)

Call useState at the top level of your component to declare a state variable.

[... 전체 내용, 모든 섹션 포함 ...]
```

#### useState.context.md (AI 최적화)
```markdown
---
title: "useState - React Reference"
url: "https://react.dev/reference/react/useState"
topics: ["React", "Hooks", "State Management"]
summary: |
  useState는 컴포넌트에 상태를 추가하는 React Hook.
  초기값을 받아 [상태, setter] 배열을 반환.
main_points:
  - 상태와 setter 함수를 배열로 반환
  - 초기 상태는 첫 렌더링에서만 사용
  - 상태 업데이트는 비동기 처리
content_type: "documentation"
difficulty: "beginner"
---

# useState - React Reference

## 핵심 요약

useState는 함수형 컴포넌트에 상태를 추가하는 Hook입니다.
초기값을 받아 [상태, setter] 배열을 반환하며, setter 호출 시 리렌더링을 트리거합니다.

## 주요 내용

### 기본 사용법
[핵심만 간결하게...]

## 핵심 인사이트
[...]
```

---

## 17. 듀얼 모드 - 여러 문서 일괄 처리

### 시나리오
여러 기술 문서를 원본과 AI 최적화 버전 모두 생성하고 싶습니다.

### 실행
```
You: 이 React Hooks 문서들 전부 원본이랑 AI 최적화 버전 둘 다 만들어줘
- https://react.dev/reference/react/useState
- https://react.dev/reference/react/useEffect
- https://react.dev/reference/react/useContext

Claude: 듀얼 모드로 3개 문서를 변환하겠습니다.
총 6개 파일이 생성됩니다.

[변환 중...]

✅ 완료!

docs/react-hooks/
├── useState.md                (3,500 글자)
├── useState.context.md        (2,100 글자)
├── useEffect.md               (4,200 글자)
├── useEffect.context.md       (2,500 글자)
├── useContext.md              (3,800 글자)
└── useContext.context.md      (2,300 글자)

통계:
- 원본 파일: 11,500 글자
- AI 최적화: 6,900 글자 (40% 절감)
- 총 6개 파일
```

### 활용 방법

```
# 사람이 학습할 때
You: useState에 대해 자세히 알려줘

Claude: [useState.md 파일을 읽음]
useState에 대한 전체 설명입니다...
[원본의 모든 내용 제공]

# AI에게 질문할 때
You: useState와 useReducer의 차이점을 비교해줘

Claude: [useState.context.md와 useReducer.context.md 읽음]
프론트매터를 통해 빠르게 각 Hook의 핵심을 파악했습니다:

- useState: 단순 상태 관리, 초기값 직접 설정
- useReducer: 복잡한 상태 로직, reducer 함수로 관리

주요 차이점:
1. [구조화된 문서에서 추출한 정확한 정보]
2. [...]

원본 파일보다 60% 빠르게 답변 생성 (토큰 절감 효과)
```

---

## 18. 듀얼 모드 - 폴더 구조 분리

### 시나리오
원본과 AI 최적화 버전을 폴더로 명확히 구분하고 싶습니다.

### 실행
```
You: 이 문서들을 원본은 docs/original/ 폴더에, AI 최적화는 docs/optimized/ 폴더에 저장해줘
- https://example.com/guide1
- https://example.com/guide2
- https://example.com/guide3

Claude: 듀얼 모드로 폴더 구조를 분리하여 저장하겠습니다.

✅ 완료!

docs/
├── original/
│   ├── guide1.md
│   ├── guide2.md
│   └── guide3.md
└── optimized/
    ├── guide1.md
    ├── guide2.md
    └── guide3.md

이제 용도에 따라 폴더를 선택하여 사용하세요:
- original/: 사람이 읽을 때
- optimized/: AI가 처리할 때
```

### 장점
- 명확한 구분
- 파일명 충돌 없음
- 관리 용이

---

## 19. 듀얼 모드 - 블로그 글 아카이빙

### 시나리오
자신의 블로그 글을 백업하면서 나중에 AI에게 질문할 수 있도록 준비합니다.

### 실행
```
You: 내 블로그 글 전체를 백업하는데, 나중에 내가 다시 읽을 용도랑 AI에게 물어볼 용도로 둘 다 만들어줘
- https://myblog.com/post1
- https://myblog.com/post2
- https://myblog.com/post3
[... 총 50개 글]

Claude: 듀얼 모드로 50개 블로그 글을 변환하겠습니다.

[변환 중... 1/50]
[변환 중... 2/50]
...
[변환 중... 50/50]

✅ 완료!

blog-archive/
├── for-reading/           # 사람이 읽을 원본
│   ├── 2024-01-15-post1.md
│   ├── 2024-01-20-post2.md
│   └── ... (50개)
└── for-ai/                # AI 질문 답변용
    ├── 2024-01-15-post1.context.md
    ├── 2024-01-20-post2.context.md
    └── ... (50개)

총 100개 파일
- 원본: 약 250,000 글자
- AI 최적화: 약 150,000 글자 (40% 절감)
```

### 활용 예시

```
3개월 후...

You: 내가 예전에 React Hooks에 대해 뭐라고 썼더라?

AI: [blog-archive/for-ai/ 폴더의 .context.md 파일들 검색]
프론트매터의 topics 필드에서 "React Hooks"를 찾았습니다.

2024-03-10-understanding-react-hooks.context.md

핵심 내용:
- useState의 기본 개념
- useEffect 활용 사례
- Custom Hooks 작성법

전체 글을 읽으시려면:
[View original](blog-archive/for-reading/2024-03-10-understanding-react-hooks.md)
```

---

## 20. 듀얼 모드 - RAG 시스템 + 사람 문서 동시 구축

### 시나리오
회사 내부 지식 베이스를 구축하는데, 직원들이 읽을 문서와 AI 시스템용 문서를 동시에 준비합니다.

### 실행
```
You: 회사 문서들을 직원용과 AI 시스템용으로 둘 다 만들어줘
- 내부 API 문서 (20개)
- 프로세스 가이드 (15개)
- 기술 스택 문서 (10개)

Claude: 듀얼 모드로 45개 문서를 변환하겠습니다.

[변환 진행...]

✅ 완료!

company-knowledge-base/
├── employee-docs/         # 직원들이 읽을 문서
│   ├── api/
│   │   ├── user-api.md
│   │   └── ... (20개)
│   ├── process/
│   │   └── ... (15개)
│   └── tech-stack/
│       └── ... (10개)
└── ai-system/             # RAG 시스템용
    ├── api/
    │   ├── user-api.context.md
    │   └── ... (20개)
    ├── process/
    │   └── ... (15개)
    └── tech-stack/
        └── ... (10개)
```

### 시스템 통합

```
[직원이 사용할 때]
내부 포털 → employee-docs/ 폴더 → 사람이 읽기 편한 원본

[AI 챗봇이 답변할 때]
직원 질문 → RAG 시스템 → ai-system/ 폴더의 .context.md 파일들 검색
→ 프론트매터로 빠른 필터링 → 관련 섹션만 추출 → 답변 생성

효과:
- 토큰 비용 40% 절감
- 답변 속도 2배 향상
- 정확도 30% 개선 (구조화된 데이터)
```

---

## 고급 활용 팁

### 1. 배치 처리 스크립트
```
You: urls.txt 파일에 있는 모든 URL을 마크다운으로 변환해줘

Claude: [파일 읽기 → 각 URL 변환 → 저장]
✅ 25개 URL 변환 완료!
```

### 2. 정기 백업
```
You: 매주 월요일마다 이 URL들을 weekly-backups 폴더에 날짜별로 저장해줘
[자동화 설정]
```

### 3. 컨텐츠 비교
```
You: 이 두 버전의 문서를 비교해줘
- https://docs.com/v1/guide (현재 v1-guide.md)
- https://docs.com/v2/guide

Claude: [v2 변환 → diff 비교 → 변경사항 요약]
```

---

## 팁 모음

1. **폴더 구조화**: 주제별로 폴더를 만들어 체계적으로 관리
2. **일관된 파일명**: 규칙적인 네이밍 컨벤션 사용
3. **메타데이터 추가**: 프론트매터에 URL, 날짜, 태그 포함
4. **정기 업데이트**: 중요한 문서는 주기적으로 재변환
5. **백업**: 변환한 파일들을 git으로 버전 관리

---

이 예제들을 참고하여 자신만의 활용법을 찾아보세요!
