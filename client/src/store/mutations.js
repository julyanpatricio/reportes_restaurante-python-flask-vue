import * as types from './mutations-types'

export default {
  [types.GET_SALES] (state, { sales, totalSales }) {
    console.log(totalSales);
    state.sales = sales
    state.totalSales = totalSales
  },
  [types.GET_SALES_BY_CATEGORIES] (state, { salesByCategories }) {
    state.salesByCategories = salesByCategories
  },
  [types.GET_SALES_BY_PRODUCTS] (state, { salesByProducts }) {
    state.salesByProducts = salesByProducts
  },
  [types.GET_SALES_BY_WAITERS] (state, { salesByWaiters }) {
    state.salesByWaiters = salesByWaiters
  }
}
