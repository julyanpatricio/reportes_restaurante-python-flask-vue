import * as types from './mutations-types'

export default {
  [types.GET_VENTAS] (state, { ventas }) {
    state.ventas = ventas
  }
}
