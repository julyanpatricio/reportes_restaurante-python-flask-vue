import * as types from './mutations-types'
import axios from 'axios'

export default {
  getSales ({ commit }) {
    axios.get('http://127.0.0.1:4000/sales')
      .then(({data}) => {
        commit(types.GET_SALES, {sales: data})
      })
  },
  getSalesByCategories ({ commit }) {
    axios.get('http://127.0.0.1:4000/sales/categories')
      .then(({data}) => {
        commit(types.GET_SALES_BY_CATEGORIES, {salesByCategories: data})
      })
  }
}
