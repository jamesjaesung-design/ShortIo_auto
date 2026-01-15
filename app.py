"""
Short.io 클릭 로그 모니터링 앱
Streamlit 기반 빠른 프로토타입
"""
import streamlit as st
import pandas as pd
from transforms import map_clicks
from shortio_client import get_clicks_data

# 페이지 설정
st.set_page_config(
    page_title="Short.io 클릭 로그",
    page_icon="🔗",
    layout="wide"
)

# 타이틀
st.title("🔗 최근 30 클릭")

# 사이드바: API 설정 (선택사항)
with st.sidebar:
    st.header("⚙️ 설정")
    
    use_api = st.checkbox("실제 API 사용", value=False)
    
    if use_api:
        api_key = st.text_input(
            "Short.io API Key",
            value="",
            type="password",
            help="환경변수 SHORTIO_API_KEY에서도 읽을 수 있습니다."
        )
        domain_id = st.text_input(
            "Domain ID",
            value="",
            help="환경변수 SHORTIO_DOMAIN_ID에서도 읽을 수 있습니다."
        )
        limit = st.number_input(
            "가져올 클릭 수",
            min_value=1,
            max_value=100,
            value=30,
            step=1
        )
    else:
        api_key = None
        domain_id = None
        limit = 30

# 시간대 선택
timezone_option = st.radio(
    "시간대 선택",
    options=["UTC", "Asia/Seoul"],
    horizontal=True,
    help="UTC 또는 Asia/Seoul(KST) 시간대로 표시합니다."
)

# 데이터 가져오기
if use_api and api_key:
    raw_data, status_msg = get_clicks_data(use_api=True, api_key=api_key, domain_id=domain_id, limit=limit)
else:
    raw_data, status_msg = get_clicks_data(use_api=False)

# 상태 메시지 표시
st.info(status_msg)

# 데이터 변환
if raw_data:
    try:
        transformed_data = map_clicks(raw_data, tz=timezone_option)
        
        if transformed_data:
            # DataFrame 생성
            df = pd.DataFrame(transformed_data)
            
            # 컬럼 순서 지정
            df = df[["link", "date", "time", "path", "city"]]
            
            # 컬럼명 한글화 (선택사항)
            df_display = df.copy()
            df_display.columns = ["링크", "날짜", "시간", "경로", "도시"]
            
            # 테이블 표시
            st.subheader(f"📊 클릭 데이터 ({len(transformed_data)}개)")
            st.dataframe(
                df_display,
                use_container_width=True,
                hide_index=True
            )
            
            # CSV 다운로드 버튼
            csv = df.to_csv(index=False).encode('utf-8-sig')  # 한글 깨짐 방지
            st.download_button(
                label="📥 CSV 다운로드",
                data=csv,
                file_name=f"shortio_clicks_{timezone_option.lower()}.csv",
                mime="text/csv",
                help="현재 표시된 데이터를 CSV 파일로 다운로드합니다."
            )
            
            # 통계 정보
            with st.expander("📈 통계 정보"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("총 클릭 수", len(transformed_data))
                with col2:
                    cities_count = len([x for x in transformed_data if x["city"]])
                    st.metric("도시 정보 있는 클릭", cities_count)
                with col3:
                    paths_count = len([x for x in transformed_data if x["path"]])
                    st.metric("경로 정보 있는 클릭", paths_count)
        else:
            st.warning("변환된 데이터가 없습니다.")
    
    except Exception as e:
        st.error(f"데이터 변환 중 오류 발생: {str(e)}")
        st.exception(e)
else:
    st.warning("데이터를 가져올 수 없습니다.")

# 하단 정보
st.markdown("---")
st.caption("💡 이 앱은 Short.io 클릭 로그에서 필요한 정보만 추출하여 표시합니다. 민감한 정보(IP, User-Agent 등)는 표시되지 않습니다.")
