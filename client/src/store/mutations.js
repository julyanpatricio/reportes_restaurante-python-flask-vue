import * as types from './mutations-types'

export default {
  [types.GET_SALES] (state, { sales, totalSales, dateMin, dateMax }) {
    state.sales = sales
    state.totalSales = totalSales
    state.dateMin = dateMin
    state.dateMax = dateMax
  },
  [types.GET_SALES_BY_CATEGORIES] (state, { salesByCategories }) {
    state.salesByCategories = salesByCategories
  },
  [types.GET_SALES_BY_PRODUCTS] (state, { salesByProducts }) {
    state.salesByProducts = salesByProducts
  },
  [types.GET_SALES_BY_WAITERS] (state, { salesByWaiters }) {
    state.salesByWaiters = salesByWaiters
  },
  [types.SET_DATE_MIN_SELECTED] (state, { dateMinSelected }) {
    state.dateMinSelected = dateMinSelected
  },
  [types.SET_DATE_MAX_SELECTED] (state, { dateMaxSelected }) {
    state.dateMaxSelected = dateMaxSelected
  }
}
