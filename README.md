# Short Auto

## 버전 정보

- **현재 버전**: v1.1.0
- **최종 업데이트**: 2026-01-12

## 프로젝트 소개

Short.io Clickstream 실시간 모니터링 대시보드입니다.
Next.js (TypeScript) + Vercel 환경에서 실행됩니다.

## 기술 스택

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Deployment**: Vercel
- **Date Library**: dayjs (with UTC & timezone plugins)

## 설치 및 실행

### 1. 패키지 설치

```bash
npm install
```

필요한 패키지:

- `next`: Next.js 프레임워크
- `react`, `react-dom`: React 라이브러리
- `dayjs`: 날짜/시간 처리 라이브러리
- `typescript`: TypeScript 컴파일러

### 2. 개발 서버 실행

```bash
npm run dev
```

개발 서버는 `http://localhost:3000`에서 실행됩니다.

### 3. 프로덕션 빌드

```bash
npm run build
npm start
```

## API 엔드포인트

### GET /api/shortio/clicks

Short.io 클릭 로그를 변환하여 반환합니다.

**Query Parameters:**

- `tz` (optional): 타임존 옵션 (`"UTC"` | `"Asia/Seoul"`), 기본값: `"UTC"`

**예시:**

```bash
# UTC 타임존으로 요청
curl http://localhost:3000/api/shortio/clicks

# Asia/Seoul 타임존으로 요청
curl http://localhost:3000/api/shortio/clicks?tz=Asia/Seoul
```

**응답 형식:**

```json
{
  "success": true,
  "data": [
    {
      "link": "https://app.short.cm/login",
      "date": "2020-05-20",
      "time": "06:19:12",
      "path": "/login",
      "city": "Mumbai"
    }
  ],
  "count": 3,
  "timezone": "UTC"
}
```

## 프로젝트 구조

```
short_auto/
├── app/
│   ├── api/
│   │   └── shortio/
│   │       └── clicks/
│   │           └── route.ts      # API 라우트
│   ├── layout.tsx                 # 루트 레이아웃
│   ├── page.tsx                   # 메인 페이지
│   └── globals.css                # 전역 스타일
├── lib/
│   └── shortioClicks.ts           # 타입 정의 및 변환 함수
├── package.json
├── tsconfig.json
├── next.config.js
└── vercel.json
```

## 주요 기능

### 1. 데이터 변환 (`lib/shortioClicks.ts`)

- Short.io 원본 클릭 데이터를 UI/API용 형태로 변환
- 타임존 변환 지원 (UTC / Asia/Seoul)
- 필수 필드만 추출 (link, date, time, path, city)
- 민감정보(ip, ua 등) 제외

### 2. API 라우트 (`app/api/shortio/clicks/route.ts`)

- Next.js App Router 기반 API 엔드포인트
- 현재는 샘플 데이터 사용 (실제 Short.io API 연동 준비됨)

## 배포

이 프로젝트는 Vercel을 통해 배포됩니다.

### 깃허브 연결 방법

1. 깃허브에서 새 저장소를 생성합니다.
2. 다음 명령어로 원격 저장소를 연결합니다:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Vercel 배포 방법

1. [Vercel](https://vercel.com)에 로그인합니다.
2. "New Project"를 클릭합니다.
3. 깃허브 저장소를 선택합니다.
4. 프로젝트 설정을 확인하고 "Deploy"를 클릭합니다.
