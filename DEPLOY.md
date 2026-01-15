# Streamlit Cloud 배포 가이드

## Streamlit Cloud 배포 방법

### 1. Streamlit Cloud 준비
1. [Streamlit Cloud](https://streamlit.io/cloud)에 접속
2. GitHub 계정으로 로그인
3. "New app" 버튼 클릭

### 2. 저장소 연결
1. GitHub 저장소 선택: `jamesjaesung-design/ShortIo_auto`
2. Branch: `main` 선택
3. Main file path: `app.py` 입력

### 3. 환경변수 설정 (선택사항)
실제 Short.io API를 사용하려면 환경변수를 설정하세요:

- **SHORTIO_API_KEY**: Short.io API 키
- **SHORTIO_DOMAIN_ID**: 도메인 ID (선택사항)

설정 방법:
1. Streamlit Cloud 대시보드에서 앱 선택
2. "Settings" → "Secrets" 클릭
3. 다음 형식으로 입력:
```
SHORTIO_API_KEY=your_api_key_here
SHORTIO_DOMAIN_ID=your_domain_id_here
```

### 4. 배포
1. "Deploy" 버튼 클릭
2. 배포 완료 후 제공되는 URL로 접속

## 배포 후 확인사항

- ✅ 앱이 정상적으로 로드되는지 확인
- ✅ Mock 데이터가 표시되는지 확인
- ✅ 시간대 변환 기능 테스트
- ✅ CSV 다운로드 기능 테스트
- ✅ 실제 API 사용 시 환경변수 설정 확인

## 문제 해결

### 배포 실패 시
1. `requirements.txt`에 모든 의존성이 포함되어 있는지 확인
2. `app.py` 파일 경로가 올바른지 확인
3. Python 버전 호환성 확인 (Python 3.9 이상 필요)

### 환경변수 미적용 시
1. Streamlit Cloud에서 "Secrets" 설정 확인
2. 앱 재배포 (Redeploy)

## 로컬 테스트

배포 전 로컬에서 테스트:
```bash
pip install streamlit pandas requests
streamlit run app.py
```
