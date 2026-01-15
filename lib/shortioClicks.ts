import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';

dayjs.extend(utc);
dayjs.extend(timezone);

/**
 * Short.io API에서 받은 원본 클릭 데이터 타입
 */
export interface ShortIoClickRaw {
  host?: string;
  path?: string;
  method?: string;
  url: string;
  dt: string; // ISO 8601 형식: '2020-05-20T06:19:12.000Z'
  st?: number;
  ip?: string;
  proto?: string;
  ref?: string;
  ua?: string;
  human?: boolean;
  browser?: string;
  browser_version?: string;
  country?: string;
  city?: string;
  social?: string;
  refhost?: string;
  os?: string;
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
  goal_completed?: boolean | null;
  ab_path?: string | null;
  lcpath?: string;
}

/**
 * UI/API에서 사용할 변환된 클릭 데이터 타입
 */
export interface ShortIoClickView {
  link: string;      // url
  date: string;      // YYYY-MM-DD
  time: string;      // HH:mm:ss
  path: string;      // path || lcpath || ""
  city: string;      // city || ""
}

/**
 * Short.io 원본 클릭 데이터 배열을 UI/API용 형태로 변환
 * 
 * @param raw - Short.io API에서 받은 원본 클릭 데이터 배열
 * @param tz - 타임존 옵션 ("UTC" | "Asia/Seoul"), 기본값: "UTC"
 * @returns 변환된 클릭 데이터 배열
 */
export function mapClicks(
  raw: ShortIoClickRaw[],
  tz: "UTC" | "Asia/Seoul" = "UTC"
): ShortIoClickView[] {
  return raw.map((click) => {
    // 1. 링크(URL)
    const link = click.url || "";

    // 2. 날짜/시간 파싱
    let date = "";
    let time = "";
    
    try {
      if (click.dt) {
        const dt = tz === "Asia/Seoul" 
          ? dayjs(click.dt).tz("Asia/Seoul")
          : dayjs.utc(click.dt);
        
        if (dt.isValid()) {
          date = dt.format("YYYY-MM-DD");
          time = dt.format("HH:mm:ss");
        }
      }
    } catch (error) {
      // 파싱 실패 시 date/time은 ""로 유지 (throw 금지)
      console.warn(`Failed to parse dt: ${click.dt}`, error);
    }

    // 3. 경로: path || lcpath || ""
    const path = click.path || click.lcpath || "";

    // 4. 도시: city || ""
    const city = click.city || "";

    return {
      link,
      date,
      time,
      path,
      city,
    };
  });
}

/**
 * 테스트/사용 예시 함수
 */
export function testMapClicks() {
  const sampleRaw: ShortIoClickRaw[] = [
    {
      host: 'shortcm.xyz',
      path: '/login',
      method: 'GET',
      url: 'https://app.short.cm/login',
      dt: '2020-05-20T06:19:12.000Z',
      st: 302,
      ip: '202.83.57.227',
      proto: 'https',
      ref: 'https://blog-short-io.cdn.ampproject.org/v/s/blog.short.io/shortlinks-youtube/amp/?amp_js_v=a3&amp_gsa=1&usqp=mq331AQFKAGwASA%3D',
      ua: 'Mozilla/5.0 ...',
      human: true,
      browser: 'Chrome Mobile',
      browser_version: '81',
      country: 'India',
      city: 'Mumbai',
      social: '',
      refhost: 'blog-short-io.cdn.ampproject.org',
      os: 'Android',
      utm_source: '',
      utm_medium: 'unknown',
      utm_campaign: '',
      goal_completed: null,
      ab_path: null,
      lcpath: '/login'
    },
    {
      url: 'https://app.short.cm/dashboard',
      dt: '2020-05-20T15:30:45.000Z',
      country: 'South Korea',
      // city 없음, path 없음, lcpath 있음
      lcpath: '/dashboard'
    }
  ];

  console.log("=== UTC 변환 결과 ===");
  const utcResult = mapClicks(sampleRaw, "UTC");
  console.log(JSON.stringify(utcResult, null, 2));

  console.log("\n=== Asia/Seoul 변환 결과 ===");
  const kstResult = mapClicks(sampleRaw, "Asia/Seoul");
  console.log(JSON.stringify(kstResult, null, 2));

  return { utcResult, kstResult };
}
