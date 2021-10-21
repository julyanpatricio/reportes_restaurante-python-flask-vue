import * as types from './mutations-types'
import axios from 'axios'

export default {
  getSales ({ commit }, {page, dateStart, dateEnd}) {
    if(dateStart){
      return axios.get(`http://127.0.0.1:4000/sales?page=${page}&date_start=${dateStart}&date_end=${dateEnd}`)
      .then(({data}) => {
        commit(types.GET_SALES, {sales: data['sales'],totalSales:data['total'], dateMin:data['dateMin'], dateMax:data['dateMax']})
      })
    }
    axios.get(`http://127.0.0.1:4000/sales?page=${page}`)
      .then(({data}) => {
        commit(types.GET_SALES, {sales: data['sales'],totalSales:data['total'], dateMin:data['dateMin'], dateMax:data['dateMax']})
      })
  },
  getSalesByCategories ({ commit }) {
    axios.get('http://127.0.0.1:4000/sales/categories')
      .then(({data}) => {
        commit(types.GET_SALES_BY_CATEGORIES, {salesByCategories: data})
      })
  },
  getSalesByProducts ({ commit }) {
    axios.get('http://127.0.0.1:4000/sales/products')
      .then(({data}) => {
        commit(types.GET_SALES_BY_PRODUCTS, {salesByProducts: data})
      })
  },
  getSalesByWaiters ({ commit }) {
    axios.get('http://127.0.0.1:4000/sales/waiters')
      .then(({data}) => {
        commit(types.GET_SALES_BY_WAITERS, {salesByWaiters: data})
      })
  }
}
