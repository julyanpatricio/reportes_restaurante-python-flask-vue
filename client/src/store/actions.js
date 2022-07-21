import * as types from './mutations-types'
import axios from 'axios'

export default {
  getDateMinAndDateMax ({ commit }) {
    axios.get(`http://127.0.0.1:4000/date_min_and_date_max`)
      .then(({data}) => {
        commit(types.GET_DATE_MIN_AND_DATE_MAX, {dateMin: data['dateMin'], dateMax: data['dateMax']})
      })
  },
  getSales ({ commit }, {page, dateStart, dateEnd}) {
    if (dateStart) {
      return axios.get(`http://127.0.0.1:4000/sales?page=${page}&date_start=${dateStart}&date_end=${dateEnd}`)
        .then(({data}) => {
          commit(types.GET_SALES, {sales: data['sales'], totalSales: data['total'], dateMin: data['dateMin'], dateMax: data['dateMax']})
        })
    }
    axios.get(`http://127.0.0.1:4000/sales?page=${page}`)
      .then(({data}) => {
        commit(types.GET_SALES, {sales: data['sales'], totalSales: data['total'], dateMin: data['dateMin'], dateMax: data['dateMax']})
      })
  },
  getSalesByCategories ({ commit }, { dateStart, dateEnd }) {
    if (dateStart) {
      return axios.get(`http://127.0.0.1:4000/sales/categories?date_start=${dateStart}&date_end=${dateEnd}`)
        .then(({data}) => {
          commit(types.GET_SALES_BY_CATEGORIES, {salesByCategories: data})
        })
    }
    axios.get('http://127.0.0.1:4000/sales/categories')
      .then(({data}) => {
        commit(types.GET_SALES_BY_CATEGORIES, {salesByCategories: data})
      })
  },
  getSalesByProducts ({ commit }, { dateStart, dateEnd }) {
    if (dateStart) {
      return axios.get(`http://127.0.0.1:4000/sales/products?date_start=${dateStart}&date_end=${dateEnd}`)
        .then(({data}) => {
          commit(types.GET_SALES_BY_PRODUCTS, {salesByProducts: data})
        })
    }
    axios.get(`http://127.0.0.1:4000/sales/products`)
      .then(({data}) => {
        commit(types.GET_SALES_BY_PRODUCTS, {salesByProducts: data})
      })
  },
  getSalesByWaiters ({ commit }, { dateStart, dateEnd }) {
    if (dateStart) {
      return axios.get(`http://127.0.0.1:4000/sales/waiters?date_start=${dateStart}&date_end=${dateEnd}`)
        .then(({data}) => {
          commit(types.GET_SALES_BY_WAITERS, {salesByWaiters: data})
        })
    }
    axios.get('http://127.0.0.1:4000/sales/waiters')
      .then(({data}) => {
        commit(types.GET_SALES_BY_WAITERS, {salesByWaiters: data})
      })
  },
  setDateMinSelected ({ commit }, { dateMinSelected }) {
    commit(types.SET_DATE_MIN_SELECTED, {dateMinSelected: dateMinSelected})
  },
  setDateMaxSelected ({ commit }, { dateMaxSelected }) {
    commit(types.SET_DATE_MAX_SELECTED, {dateMaxSelected: dateMaxSelected})
  }
}
