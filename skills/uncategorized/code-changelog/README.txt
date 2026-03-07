# Code Changelog + HonKit Documentation Server

매 수정마다 reviews 폴더에 문서를 생성하고 HonKit으로 아름다운 문서 서버를 자동으로 빌드합니다.

## 🎯 특징

✅ **자동 문서 생성**: 매 수정마다 MD 파일 생성
✅ **HonKit 통합**: GitBook 스타일의 문서 사이트
✅ **자동 네비게이션**: SUMMARY.md 자동 업데이트
✅ **실시간 서버**: http://localhost:4000
✅ **검색 기능**: 전체 문서 검색 가능

## 🚀 빠른 시작

### 1. HonKit 설치 (최초 1회)
```bash
npm install -g honkit
```

### 2. Python에서 사용
```python
from code_changelog_tracker import CodeChangeLogger

logger = CodeChangeLogger("프로젝트명")
logger.log_file_creation("main.py", "코드", "이유")
logger.save_and_build()  # 저장 + 빌드!
```

### 3. 문서 서버 실행
```bash
cd reviews
honkit serve

# 브라우저: http://localhost:4000
```

## 📁 구조

```
reviews/
├── README.md          # 홈페이지
├── SUMMARY.md         # 네비게이션 (자동 생성)
├── book.json          # HonKit 설정
├── 20251020_140000.md # 변경 이력 1
├── 20251020_140530.md # 변경 이력 2
└── ...

_book/                 # 빌드된 사이트
├── index.html
└── ...
```

## 💡 사용법

### 기본 사용
```python
logger = CodeChangeLogger("Todo App")

# 작업 1
logger.log_file_creation("app.py", "...", "Flask 설정")
logger.save_and_build()

# 작업 2
logger.log_file_modification("app.py", "old", "new", "기능 추가")
logger.save_and_build()

# 브라우저에서 확인: http://localhost:4000
```

### 명령줄 인터페이스
```bash
# 초기화
python code_changelog_tracker.py init

# 빌드만
python code_changelog_tracker.py build

# 서버 실행
python code_changelog_tracker.py serve
```

## 🌐 문서 사이트 기능

- 📚 **목차**: 날짜/시간별 자동 분류
- 🔍 **검색**: 전체 문서 검색
- 📱 **반응형**: 모바일 지원
- 🎨 **테마**: GitBook 스타일
- ⬅️➡️ **네비게이션**: 이전/다음 페이지

## API

### 초기화
```python
logger = CodeChangeLogger(
    project_name="프로젝트명",
    user_request="요구사항",
    reviews_dir="reviews",
    port=4000  # 선택, 기본 4000
)
```

### 기록 메서드
```python
logger.log_file_creation(file_path, content, reason)
logger.log_file_modification(file_path, old, new, reason)
logger.log_file_deletion(file_path, content, reason)
logger.log_bug_fix(file_path, old, new, bug_desc, fix_desc)
logger.log_refactoring(file_path, old, new, type, reason)
```

### 저장 및 빌드
```python
# 저장만
logger.save_review()

# 저장 + SUMMARY 업데이트
logger.save_and_update()

# 저장 + SUMMARY + 빌드 (권장)
logger.save_and_build()
```

## 🔧 HonKit 명령어

```bash
# 설치
npm install -g honkit

# 빌드
cd reviews
honkit build

# 서버 (자동 새로고침)
honkit serve

# 커스텀 포트
honkit serve --port 3000
honkit serve --port 8080
```

## 🔌 포트 설정

```bash
# Python 코드
logger = CodeChangeLogger("프로젝트", port=3000)
logger.serve_docs()  # → http://localhost:3000

# 명령줄
python code_changelog_tracker.py serve --port 3000

# 자동 포트 찾기 (기본)
python code_changelog_tracker.py serve
# 포트 4000이 사용 중이면 자동으로 4001, 4002... 찾음
```

## 📦 배포

### GitHub Pages
```bash
python code_changelog_tracker.py build
git add _book
git subtree push --prefix _book origin gh-pages
```

### Netlify
```toml
# netlify.toml
[build]
  command = "cd reviews && honkit build"
  publish = "_book"
```

## 전체 문서

SKILL.md에 완전한 구현 코드와 상세 가이드가 포함되어 있습니다.

---

**매 수정마다 아름다운 문서 사이트로!** 🎉
