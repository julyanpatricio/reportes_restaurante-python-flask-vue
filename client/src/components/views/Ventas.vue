<template>
  <div v-if='ventas'>
    <h1>ventas</h1>
    <ul>
      <li v-for='(venta, i) in ventas' :key='i'>
        id: {{venta.id}} - total: {{venta.total}}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    ventas: null
  }),
  async created () {
    const {data} = await axios.get('http://127.0.0.1:4000/ventas')
    console.log(data)
    this.ventas = data
  }
}
</script>
