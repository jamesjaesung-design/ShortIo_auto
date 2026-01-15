"""
Short.io API 클라이언트 모듈
실제 API 호출 또는 mock 데이터 제공
"""
import os
import json
from typing import List, Dict, Any


def get_mock_data() -> List[Dict[str, Any]]:
    """
    Mock 데이터 반환 (테스트용)
    """
    return [
        {
            "host": "shortcm.xyz",
            "path": "/login",
            "method": "GET",
            "url": "https://app.short.cm/login",
            "dt": "2020-05-20T06:19:12.000Z",
            "st": 302,
            "ip": "202.83.57.227",
            "proto": "https",
            "ref": "https://blog-short-io.cdn.ampproject.org/v/s/blog.short.io/shortlinks-youtube/amp/?amp_js_v=a3&amp_gsa=1&usqp=mq331AQFKAGwASA%3D",
            "ua": "Mozilla/5.0 (Linux; Android 10; HD1901)...",
            "human": True,
            "browser": "Chrome Mobile",
            "browser_version": "81",
            "country": "India",
            "city": "Mumbai",
            "social": "",
            "refhost": "blog-short-io.cdn.ampproject.org",
            "os": "Android",
            "utm_source": "",
            "utm_medium": "unknown",
            "utm_campaign": "",
            "goal_completed": None,
            "ab_path": None,
            "lcpath": "/login"
        },
        {
            "host": "shortcm.xyz",
            "path": "/dashboard",
            "method": "GET",
            "url": "https://app.short.cm/dashboard",
            "dt": "2020-05-20T15:30:45.000Z",
            "st": 200,
            "ip": "123.456.789.012",
            "proto": "https",
            "ref": "",
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            "human": True,
            "browser": "Chrome",
            "browser_version": "90",
            "country": "South Korea",
            # city 필드 없음
            "social": "",
            "refhost": "",
            "os": "Windows",
            "utm_source": "",
            "utm_medium": "",
            "utm_campaign": "",
            "goal_completed": None,
            "ab_path": None,
            "lcpath": "/dashboard"
        },
        {
            "host": "shortcm.xyz",
            "method": "GET",
            "url": "https://app.short.cm/settings",
            "dt": "2020-05-20T20:45:30.000Z",
            "st": 200,
            "country": "United States",
            "city": "New York",
            # path 없음, lcpath만 있음
            "lcpath": "/settings"
        },
        {
            "host": "shortcm.xyz",
            "path": "/api/data",
            "url": "https://app.short.cm/api/data",
            "dt": "2020-05-21T08:15:22.000Z",
            "country": "Japan",
            "city": "Tokyo"
        },
        {
            "host": "shortcm.xyz",
            "url": "https://app.short.cm/products",
            "dt": "2020-05-21T12:30:10.000Z",
            "country": "Germany",
            # city 없음
            "lcpath": "/products"
        }
    ]


def fetch_last_clicks(api_key: str = None, domain_id: str = None, limit: int = 30) -> List[Dict[str, Any]]:
    """
    Short.io API에서 최근 클릭 로그를 가져옴
    
    Args:
        api_key: Short.io API 키 (환경변수 SHORTIO_API_KEY에서도 읽음)
        domain_id: 도메인 ID (환경변수 SHORTIO_DOMAIN_ID에서도 읽음)
        limit: 가져올 클릭 수 (기본값: 30)
    
    Returns:
        클릭 로그 리스트
    
    Raises:
        Exception: API 호출 실패 시
    """
    # 환경변수에서 읽기
    api_key = api_key or os.getenv("SHORTIO_API_KEY")
    domain_id = domain_id or os.getenv("SHORTIO_DOMAIN_ID")
    
    # API 키가 없으면 mock 데이터 반환
    if not api_key:
        return get_mock_data()
    
    # 실제 API 호출
    try:
        import requests
        
        url = f"https://api-v2.short.io/statistics/domain/{domain_id}/last_clicks"
        payload = {
            "limit": limit,
            "include": {"human": True}
        }
        headers = {
            "accept": "*/*",
            "content-type": "application/json",
            "authorization": api_key
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        return response.json()
    
    except Exception as e:
        # API 호출 실패 시 mock 데이터 반환하고 에러 정보 포함
        error_msg = f"API 호출 실패: {str(e)}. Mock 데이터를 사용합니다."
        print(error_msg)
        return get_mock_data()


def get_clicks_data(use_api: bool = False, api_key: str = None, domain_id: str = None, limit: int = 30) -> tuple[List[Dict[str, Any]], str]:
    """
    클릭 데이터를 가져오는 통합 함수
    
    Args:
        use_api: 실제 API 사용 여부
        api_key: API 키
        domain_id: 도메인 ID
        limit: 가져올 클릭 수
    
    Returns:
        (클릭 데이터 리스트, 상태 메시지) 튜플
    """
    if use_api and api_key:
        try:
            data = fetch_last_clicks(api_key, domain_id, limit)
            return data, "✅ 실제 API에서 데이터를 가져왔습니다."
        except Exception as e:
            return get_mock_data(), f"⚠️ API 호출 실패: {str(e)}. Mock 데이터를 사용합니다."
    else:
        return get_mock_data(), "ℹ️ Mock 데이터를 사용 중입니다. (실제 API 사용하려면 API 키를 입력하세요)"
