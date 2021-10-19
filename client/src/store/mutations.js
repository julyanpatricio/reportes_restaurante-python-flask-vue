import * as types from './mutations-types'

export default {
  [types.GET_SALES] (state, { sales }) {
    state.sales = sales
  },
  [types.GET_SALES_BY_CATEGORIES] (state, { salesByCategories }) {
    state.salesByCategories = salesByCategories
  }
}
