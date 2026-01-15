import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Short.io Clickstream 실시간 모니터링',
  description: 'Short.io 클릭 로그 모니터링 대시보드',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  )
}
