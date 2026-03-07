# Card News Generator Skill V2

한국어 텍스트를 지원하는 소셜 미디어용 카드 뉴스 이미지 생성 스킬입니다.

## 특징

### V2 새로운 기능 🆕
- ✨ **배경 이미지 지원**: 폴더의 이미지를 배경으로 자동 적용
- ✨ **Cafe24Ssurround 폰트**: 번들 폰트 포함, 별도 설치 불필요
- ✨ **자동 텍스트 색상**: 배경 이미지 사용 시 흰색으로 자동 전환
- ✨ **오버레이 조절**: 텍스트 가독성을 위한 어두운 오버레이 (조절 가능)
- ✨ **반투명 박스 + 테두리**: 텍스트 영역에 둥근 박스와 흰색 테두리
- ✨ **컴팩트 디자인**: 정사각형에 가까운 중앙 정렬 박스

### 기본 기능
- ✅ **인터랙티브 모드**: 단계별 안내로 쉽게 카드 생성
- ✅ **RGB 색상 입력**: 사용자가 직접 RGB 값으로 색상 선택
- ✅ 한글 텍스트 완벽 지원
- ✅ 자동 중앙 정렬 및 레이아웃
- ✅ 600x600 Instagram 최적화
- ✅ 다양한 이미지 크기

## 설치 방법

### 필수 패키지 설치

```bash
pip install Pillow --break-system-packages
```

### 폰트 (V2)

**V2부터는 Cafe24Ssurround 폰트가 스킬에 포함되어 있어 별도 설치가 필요 없습니다!**

폰트 위치: `skills/card-news-generator/fonts/Cafe24Ssurround-v2.0.ttf`

만약 시스템 폰트를 사용하려면 (선택사항):
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y fonts-noto-cjk fonts-noto-cjk-extra

# macOS - 시스템 폰트 자동 감지 (AppleSDGothicNeo)
```

## 파일 구조

```
card-news-generator/
├── SKILL.md              # 스킬 메타데이터 및 사용 가이드
├── generate_card.py      # 카드 생성 스크립트 (V2 - 배경 이미지 지원)
├── auto_generator.py     # 자동 카드 생성 스크립트
├── interactive_generator.py  # 인터랙티브 모드
├── fonts/                # V2: 번들 폰트
│   └── Cafe24Ssurround-v2.0.ttf
├── V2_FEATURES.md        # V2 상세 가이드
└── README.md            # 이 파일
```

## 사용 예시

### 방법 1: 자동 생성 모드 (V2 - 권장) 🆕

#### 옵션 A: 단색 배경

```bash
python auto_generator.py \
  --topic "건강 습관" \
  --bg-color "#f5f3ee" \
  --text-color "#1a1a1a" \
  --output-dir ./output \
  --base-filename "health" << 'EOF'
1. 수분 섭취
하루 8잔 이상
물 마시기 습관

2. 규칙적 운동
주 3회 이상
30분 운동하기

3. 충분한 수면
하루 7-8시간
숙면 취하기
EOF
```

#### 옵션 B: 배경 이미지 사용 (V2 신기능) ⭐

**1단계: 배경 이미지 준비**

이미지를 폴더에 순서대로 저장:
```
my-images/
├── 1.png
├── 2.png
└── 3.png
```

또는 숫자로 정렬:
```
backgrounds/
├── 01.jpg
├── 02.jpg
└── 03.jpg
```

**2단계: 카드 생성**

```bash
python auto_generator.py \
  --topic "서울 부동산" \
  --output-dir ./output \
  --base-filename "realestate" \
  --image-folder ./my-images \
  --overlay-opacity 0.6 << 'EOF'
1. 가격 상승세
2023년 대비
평균 15% 상승

2. 거래량 증가
전년 동기 대비
거래 건수 20% 증가

3. 향후 전망
금리 안정화로
안정세 예상
EOF
```

**주요 파라미터:**
- `--image-folder`: 배경 이미지 폴더 경로
- `--overlay-opacity`: 오버레이 불투명도 (0.0~1.0)
  - `0.3`: 밝은 이미지
  - `0.6`: 보통 이미지 (권장)
  - `0.8`: 어두운 이미지

### 방법 2: 인터랙티브 모드

사용자가 단계별로 입력하는 방식:

```bash
python interactive_generator.py
```

프롬프트에 따라 다음을 입력:
1. 제목 (여러 줄 가능, 빈 줄로 종료)
2. 내용 (여러 줄 가능, 빈 줄로 종료)
3. 배경색 RGB (예: `245,243,238`)
4. 텍스트색 RGB (예: `26,26,26`)
5. 카드 번호 (선택사항)
6. 파일명

### 방법 3: 단일 카드 직접 생성

#### 단색 배경:

```bash
python generate_card.py \
  --title "수분 섭취" \
  --content "하루 8잔 이상\n물 마시기 습관" \
  --bg-color "#f5f3ee" \
  --text-color "#1a1a1a" \
  --output ./output/card.png
```

#### 배경 이미지 (V2): 🆕

```bash
python generate_card.py \
  --title "가격 상승세" \
  --content "2023년 대비\n평균 15% 상승" \
  --bg-image ./my-images/1.png \
  --overlay-opacity 0.6 \
  --output ./output/card.png
```

## 파라미터 설명

### 필수 파라미터
- `--title`: 카드의 메인 제목 (줄바꿈은 `\n` 사용)
- `--content`: 본문 내용 (줄바꿈은 `\n` 사용)
- `--output`: 저장할 파일 경로

### 선택 파라미터 (기본)
- `--bg-color`: 배경색 (기본값: `#F5F3EE`)
- `--text-color`: 텍스트 색상 (기본값: `#1A1A1A`)
- `--width`: 이미지 너비 (기본값: 600)
- `--height`: 이미지 높이 (기본값: 600)
- `--title-size`: 제목 폰트 크기 (기본값: 48)
- `--content-size`: 본문 폰트 크기 (기본값: 28)

### V2 추가 파라미터 🆕
- `--bg-image`: 배경 이미지 파일 경로
- `--overlay-opacity`: 오버레이 불투명도 (0.0~1.0, 기본값: 0.5)
- `--image-folder`: 배경 이미지 폴더 경로 (auto_generator.py)
- 텍스트가 배경 이미지 위에 반투명 박스 + 흰색 테두리로 표시됨
- 배경 이미지 사용 시 텍스트 색상 자동으로 흰색으로 변경

## 추천 배경색 (RGB 형식)

| 색상 이름 | RGB 값 | Hex 코드 | 용도 |
|---------|---------|---------|-----|
| 따뜻한 베이지 | `245,243,238` | `#f5f3ee` | 기본, 모든 주제 |
| 소프트 핑크 | `255,229,229` | `#ffe5e5` | 부드러운 주제 |
| 민트 그린 | `224,244,241` | `#e0f4f1` | 자연, 건강 |
| 라벤더 | `232,224,245` | `#e8e0f5` | 감성, 힐링 |
| 피치 | `255,232,214` | `#ffe8d6` | 따뜻함, 활력 |
| 스카이 블루 | `227,242,253` | `#e3f2fd` | 전문성, 신뢰 |

**색상 입력 방법:**
- 인터랙티브 모드: RGB 값 직접 입력 (예: `245,243,238`)
- 직접 명령어: Hex 코드 사용 (예: `#f5f3ee`)

## 해결 방법

### 한글이 깨질 때
```bash
# 폰트 재설치
sudo apt-get install --reinstall fonts-noto-cjk
fc-cache -fv
```

### PIL 모듈 에러
```bash
pip install --upgrade Pillow --break-system-packages
```

### 파일 저장 실패
- 출력 경로가 존재하는지 확인
- 쓰기 권한이 있는지 확인
- 절대 경로 사용 권장

## V2 주요 변경사항 요약

### 디자인 개선
- ✨ 반투명 검은색 박스 + 흰색 테두리로 텍스트 영역 강조
- ✨ 정사각형에 가까운 컴팩트 박스 (캔버스의 65% 너비)
- ✨ 텍스트 중앙 정렬로 배경 이미지가 양쪽에 보임

### 기술 개선
- 📦 Cafe24Ssurround 폰트 번들 포함 (별도 설치 불필요)
- 🖼️ 배경 이미지 자동 크롭 및 리사이징 (600x600)
- 🎨 오버레이 불투명도 조절 가능 (0.0~1.0)
- 🤖 배경 이미지 사용 시 텍스트 색상 자동 흰색 전환
- 🔤 macOS/Linux 자동 폰트 감지

### 지원 형식
- 배경 이미지: JPG, JPEG, PNG, WebP, BMP
- 출력 형식: PNG (600x600 Instagram 최적화)

## 스킬 로드 방법

Claude Code에서 이 스킬을 사용하려면:

1. 스킬 디렉토리를 skills 폴더에 복사
2. Claude에게 요청: "card-news-generator 스킬을 사용해서 카드를 만들어줘"
3. V2 기능 사용: "배경 이미지를 넣어서 카드 뉴스 만들어줘"

## 더 알아보기

- [V2_FEATURES.md](./V2_FEATURES.md): V2 상세 기능 가이드 및 트러블슈팅
- [SKILL.md](./SKILL.md): 스킬 메타데이터 및 자동화 워크플로우

## 라이선스

MIT License
