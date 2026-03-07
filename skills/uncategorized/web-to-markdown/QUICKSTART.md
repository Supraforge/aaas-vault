# Quick Start Guide - Web to Markdown

웹페이지를 마크다운으로 변환하는 가장 빠른 방법을 알려드립니다.

## 5초 만에 시작하기

### 1. 단일 페이지 변환

```
You: https://example.com/article 이거 마크다운으로 저장해줘

Claude: 파일명을 어떻게 할까요? (기본: webpage.md)

You: article.md

Claude: ✅ 완료!
📄 article.md 파일이 생성되었습니다.
```

### 2. 빠른 변환 (파일명 생략)

```
You: https://docs.python.org/tutorial 를 python-tutorial.md로 저장해줘

Claude: [바로 변환 및 저장]
✅ python-tutorial.md 파일이 생성되었습니다.
```

### 3. 내용만 보기

```
You: https://blog.example.com/post 내용을 마크다운으로 보여줘만

Claude: [마크다운 내용을 화면에 출력, 파일로 저장 안 함]
```

## 자주 사용하는 패턴

### 여러 페이지 한 번에

```
You: 이 URL들을 docs 폴더에 마크다운으로 저장해줘
- https://example.com/guide1
- https://example.com/guide2
- https://example.com/guide3

Claude: [docs 폴더 생성 및 각 페이지를 guide1.md, guide2.md, guide3.md로 저장]
```

### 특정 섹션만 추출

```
You: https://example.com/docs 에서 "설치 가이드" 부분만 마크다운으로 저장해줘

Claude: [해당 섹션만 추출하여 저장]
```

### 자동 파일명

```
You: https://example.com/blog/awesome-article 이거 적당한 파일명으로 저장해줘

Claude: [페이지 제목을 기반으로 자동 파일명 생성]
✅ awesome-article.md 파일이 생성되었습니다.
```

## 실전 예제

### 예제 1: 기술 문서 아카이브

```
You: 이 기술 문서들을 tech-docs 폴더에 저장해줘
- https://react.dev/learn
- https://nextjs.org/docs
- https://tailwindcss.com/docs

Claude: [tech-docs 폴더 생성]
Claude: [3개 파일 변환 및 저장]

✅ 3개의 문서가 tech-docs 폴더에 저장되었습니다:
- react-learn.md
- nextjs-docs.md
- tailwindcss-docs.md
```

### 예제 2: 블로그 포스트 백업

```
You: 내 블로그 글 https://myblog.com/posts/2024/my-post 를 백업해줘

Claude: 어디에 저장할까요?

You: backup/blog/ 폴더에 날짜 포함해서

Claude: ✅ 저장 완료!
📄 backup/blog/2024-01-15-my-post.md
```

### 예제 3: 튜토리얼 컬렉션

```
You: 파이썬 튜토리얼 시리즈를 전부 마크다운으로 저장해줘
- https://tutorial.com/python/basics
- https://tutorial.com/python/intermediate
- https://tutorial.com/python/advanced

Claude: tutorials/python/ 폴더에 저장하겠습니다.

✅ 저장 완료!
tutorials/python/
├── basics.md
├── intermediate.md
└── advanced.md
```

## Pro Tips

1. **URL만 붙여넣기**: URL만 입력해도 Claude가 알아서 처리합니다
   ```
   You: https://example.com/article
   ```

2. **파일명에 경로 포함**: 원하는 폴더를 파일명에 포함시키세요
   ```
   You: docs/guide.md로 저장해줘
   ```

3. **여러 URL 한 번에**: 줄바꿈으로 구분하여 여러 URL 입력
   ```
   You: 이것들 전부 마크다운으로
   https://url1.com
   https://url2.com
   https://url3.com
   ```

4. **빠른 미리보기**: 저장 여부를 나중에 결정
   ```
   You: https://example.com 먼저 보여줘
   [내용 확인 후]
   You: 이거 article.md로 저장해줘
   ```

## 트러블슈팅

### 문제: URL이 열리지 않음
**해결**: URL 전체를 복사했는지 확인 (`https://` 포함)

### 문제: 이상한 내용이 저장됨
**해결**: "주요 내용만 추출해서 다시 저장해줘" 요청

### 문제: 파일이 너무 큼
**해결**: "요약해서 저장해줘" 또는 "특정 섹션만 저장해줘" 요청

## 다음 단계

더 자세한 내용은 다음 문서를 참고하세요:
- `SKILL.md`: 전체 워크플로우 및 고급 기능
- `README.md`: 개요 및 활용 예시
- `EXAMPLES.md`: 다양한 실전 예제

---

**준비 완료!** 이제 웹페이지 URL을 입력하고 마크다운으로 변환해보세요.
