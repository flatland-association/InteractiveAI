import type { CorrelationResponse } from '@/entities/ORANGE/types'
import http from '@/plugins/http'
import type { Card } from '@/types/cards'

export function getCorrelations(params: { size: number; app_id?: string; kpi_name?: string }) {
  return http.get<CorrelationResponse>('cab_correlation/api/v1/correlation', {
    params
  })
}
export function sendFeedback(card: Card<'ORANGE'>, feedback: boolean) {
  const data = {
    card: card.data.metadata,
    feedback: feedback,
    feedback_date: Date.now()
  }
  return http.post('cab_correlation/api/v1/correlation/feedback', data)
}
