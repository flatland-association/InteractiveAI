import http from '@/plugins/http'
import type { Context, Entity } from '@/types/entities'
import type { ContextResponse } from '@/types/services'
import type { TraceType } from '@/types/trace'

// TODO: typing
export function getRecommendation<T>(context: Context) {
  return http.post<T>('/cab_recommendation/api/v1/recommendation', context)
}

export function getContext<E extends Entity = Entity>() {
  return http.get<ContextResponse<E>>(`/cabcontext/api/v1/contexts?time=${Date.now()}`)
}

// TODO: typing
export function sendTrace(payload: {
  data: object
  date?: Date
  step: TraceType
  use_case: Entity
}) {
  return http.post(import.meta.env.VITE_TRACE + '/api/v1/traces', {
    ...payload,
    date: new Date().toISOString()
  })
}
