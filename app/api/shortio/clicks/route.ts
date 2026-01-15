import { NextResponse } from 'next/server';
import { mapClicks, ShortIoClickRaw } from '@/lib/shortioClicks';

/**
 * GET /api/shortio/clicks
 * 
 * Short.io 클릭 로그를 변환하여 반환하는 API 엔드포인트
 * 
 * Query Parameters:
 * - tz: 타임존 옵션 ("UTC" | "Asia/Seoul"), 기본값: "UTC"
 * 
 * 현재는 샘플 데이터를 사용하며, 나중에 실제 Short.io API 호출로 교체 가능한 구조
 */
export async function GET(request: Request) {
  try {
    // Query parameter에서 타임존 옵션 추출
    const { searchParams } = new URL(request.url);
    const tz = (searchParams.get('tz') as "UTC" | "Asia/Seoul") || "UTC";

    // TODO: 실제 Short.io API 호출로 교체
    // const domainId = searchParams.get('domainId');
    // const limit = parseInt(searchParams.get('limit') || '30');
    // const response = await fetch(`https://api-v2.short.io/statistics/domain/${domainId}/last_clicks`, {
    //   method: 'POST',
    //   headers: {
    //     'accept': '*/*',
    //     'content-type': 'application/json',
    //     'authorization': process.env.SHORTIO_API_KEY || ''
    //   },
    //   body: JSON.stringify({ limit, include: { human: true } })
    // });
    // const rawData: ShortIoClickRaw[] = await response.json();

    // 임시 샘플 데이터 (실제 API 응답 형태와 동일)
    const sampleRawData: ShortIoClickRaw[] = [
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
        host: 'shortcm.xyz',
        path: '/dashboard',
        method: 'GET',
        url: 'https://app.short.cm/dashboard',
        dt: '2020-05-20T15:30:45.000Z',
        st: 200,
        ip: '123.456.789.012',
        proto: 'https',
        ref: '',
        ua: 'Mozilla/5.0 ...',
        human: true,
        browser: 'Chrome',
        browser_version: '90',
        country: 'South Korea',
        // city 필드 없음
        social: '',
        refhost: '',
        os: 'Windows',
        utm_source: '',
        utm_medium: '',
        utm_campaign: '',
        goal_completed: null,
        ab_path: null,
        lcpath: '/dashboard'
      },
      {
        host: 'shortcm.xyz',
        method: 'GET',
        url: 'https://app.short.cm/settings',
        dt: '2020-05-20T20:45:30.000Z',
        st: 200,
        country: 'United States',
        city: 'New York',
        // path 없음, lcpath만 있음
        lcpath: '/settings'
      }
    ];

    // 변환 함수 호출
    const transformedData = mapClicks(sampleRawData, tz);

    return NextResponse.json({
      success: true,
      data: transformedData,
      count: transformedData.length,
      timezone: tz,
      // 디버깅용: 원본 데이터는 제외 (민감정보 포함)
    });
  } catch (error) {
    console.error('Error processing clicks:', error);
    return NextResponse.json(
      {
        success: false,
        error: 'Failed to process clicks data',
        message: error instanceof Error ? error.message : 'Unknown error'
      },
      { status: 500 }
    );
  }
}
