import * as types from './mutations-types'
import axios from 'axios'

export default {
  getVentas ({ commit }) {
    axios.get('http://127.0.0.1:4000/ventas')
      .then(({data}) => {
        commit(types.GET_VENTAS, {ventas: data})
      })
  }
}
