import type { Card } from './cards'
import type { Action, Context, Entity } from './entities'
import type { DateMillisecondsFormat, UUID } from './formats'
export type Recommendation<T extends Entity = Entity> = {
  agent_type: 'IA'
  use_case: Entity
  description: string
  title: string
  actions: Action<T>[]
}

export type FullContext<T extends Entity = Entity> = {
  data: Context<T>
  date: DateMillisecondsFormat
  id_context: UUID
  use_case: T
}

export type TraceType = 'EVENT' | 'ASKFORHELP' | 'SOLUTION' | 'AWARD'

export type Trace = {
  data: Action | Card['id']
  date?: DateMillisecondsFormat
  id_trace?: UUID
  step: TraceType
  use_case: Entity
}
