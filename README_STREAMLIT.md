# Short.io 클릭 로그 모니터링 앱 (Streamlit)

Python + Streamlit 기반 빠른 프로토타입

## 빠른 시작

### 1. 의존성 설치
```bash
pip install streamlit pandas requests
```

또는 requirements.txt 사용:
```bash
pip install -r requirements.txt
```

### 2. 앱 실행
```bash
streamlit run app.py
```

브라우저가 자동으로 열리며 `http://localhost:8501`에서 앱이 실행됩니다.

## 기능

- ✅ Short.io 클릭 로그에서 5개 필드만 추출 (link, date, time, path, city)
- ✅ 시간대 변환 지원 (UTC / Asia/Seoul)
- ✅ 테이블 형태로 데이터 표시
- ✅ CSV 다운로드 기능
- ✅ Mock 데이터로 즉시 테스트 가능
- ✅ 실제 Short.io API 연동 지원 (선택사항)

## 파일 구조

```
short_auto/
├── app.py              # Streamlit UI 메인 파일
├── transforms.py       # 데이터 변환 함수
├── shortio_client.py   # API 클라이언트 및 mock 데이터
└── requirements.txt    # Python 의존성
```

## 사용 방법

### Mock 데이터로 테스트
1. 앱 실행: `streamlit run app.py`
2. 사이드바에서 "실제 API 사용" 체크박스를 해제
3. 시간대 선택 (UTC / Asia/Seoul)
4. 테이블 확인 및 CSV 다운로드

### 실제 API 사용
1. 사이드바에서 "실제 API 사용" 체크박스 선택
2. Short.io API Key 입력
3. Domain ID 입력 (선택사항, 환경변수로도 설정 가능)
4. 데이터 가져오기

### 환경변수 설정 (선택사항)
```bash
export SHORTIO_API_KEY="your_api_key_here"
export SHORTIO_DOMAIN_ID="your_domain_id_here"
```

## 주요 함수

### `map_clicks(raw, tz="UTC")`
- Short.io 원본 데이터를 UI용 형태로 변환
- 타임존 변환 지원
- 안전한 파싱 (예외 발생 시 빈 문자열 반환)

### `fetch_last_clicks(api_key, domain_id, limit=30)`
- Short.io API에서 최근 클릭 로그 가져오기
- API 키가 없으면 자동으로 mock 데이터 반환

## 요구사항

- Python 3.9 이상 (zoneinfo 사용)
- streamlit >= 1.28.0
- pandas >= 2.0.0
- requests >= 2.31.0 (API 사용 시)
