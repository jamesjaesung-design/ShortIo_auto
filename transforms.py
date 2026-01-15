"""
Short.io 클릭 로그 데이터 변환 모듈
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import List, Dict, Any


def map_clicks(raw: List[Dict[str, Any]], tz: str = "UTC") -> List[Dict[str, Any]]:
    """
    Short.io 원본 클릭 데이터 리스트를 UI용 형태로 변환
    
    Args:
        raw: Short.io API에서 받은 원본 클릭 데이터 리스트
        tz: 타임존 옵션 ("UTC" | "Asia/Seoul"), 기본값: "UTC"
    
    Returns:
        변환된 클릭 데이터 리스트: [{link, date, time, path, city}, ...]
    """
    result = []
    
    # 타임존 설정
    timezone = ZoneInfo(tz) if tz == "Asia/Seoul" else ZoneInfo("UTC")
    
    for click in raw:
        # 1. 링크(URL)
        link = click.get("url", "")
        
        # 2. 날짜/시간 파싱
        date = ""
        time = ""
        
        try:
            dt_str = click.get("dt", "")
            if dt_str:
                # ISO8601 형식 파싱 (Z 포함)
                dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
                # 타임존 변환
                if tz == "Asia/Seoul":
                    dt = dt.astimezone(timezone)
                else:
                    dt = dt.replace(tzinfo=ZoneInfo("UTC"))
                
                date = dt.strftime("%Y-%m-%d")
                time = dt.strftime("%H:%M:%S")
        except (ValueError, AttributeError, KeyError) as e:
            # 파싱 실패 시 date/time은 ""로 유지 (예외로 앱이 죽으면 안 됨)
            pass
        
        # 3. 경로: path가 있으면 path, 없으면 lcpath, 둘 다 없으면 ""
        path = click.get("path") or click.get("lcpath") or ""
        
        # 4. 도시: city 필드가 없으면 "" (country만 있으면 city는 "" 유지)
        city = click.get("city", "")
        
        result.append({
            "link": link,
            "date": date,
            "time": time,
            "path": path,
            "city": city,
        })
    
    # 정렬: 최신 dt 우선 (내림차순)
    # date와 time이 모두 있는 경우만 정렬에 사용
    def sort_key(item):
        date_str = item.get("date", "")
        time_str = item.get("time", "")
        if date_str and time_str:
            return f"{date_str} {time_str}"
        return ""  # 날짜/시간이 없으면 맨 뒤로
    
    result.sort(key=sort_key, reverse=True)
    
    return result
