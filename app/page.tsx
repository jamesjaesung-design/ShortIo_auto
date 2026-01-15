export default function Home() {
  return (
    <div style={{ 
      background: 'white', 
      padding: '2rem', 
      borderRadius: '10px', 
      boxShadow: '0 10px 40px rgba(0,0,0,0.2)',
      maxWidth: '1200px',
      margin: '0 auto'
    }}>
      <h1 style={{ marginBottom: '1.5rem', color: '#667eea', textAlign: 'center' }}>
        🔗 Short.io Clickstream 실시간 모니터링
      </h1>
      <p style={{ textAlign: 'center', color: '#666' }}>
        Next.js + TypeScript + Vercel 환경에서 실행 중입니다.
      </p>
      <p style={{ textAlign: 'center', marginTop: '1rem', color: '#999', fontSize: '0.9rem' }}>
        API 엔드포인트: <code>/api/shortio/clicks</code>
      </p>
    </div>
  )
}
