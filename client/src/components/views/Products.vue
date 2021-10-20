<template>
  <div v-if="salesByProducts">
    <h1>ventas por productos</h1>
    <md-table>
      <md-table-row>
        <md-table-head>Producto</md-table-head>
        <md-table-head>Categoria</md-table-head>
        <md-table-head>Cantidades vendidas</md-table-head>
        <md-table-head>Ingresos Totales</md-table-head>
      </md-table-row>

      <md-table-row  v-for="(value, key) in salesByProducts" :key="key">
        <md-table-cell>{{key}}</md-table-cell>
        <md-table-cell>{{ value['category'] }}</md-table-cell>
        <md-table-cell>{{ value['total quantities'] }}</md-table-cell>
        <md-table-cell>{{ value['total incomes'] }}</md-table-cell>
      </md-table-row>

    </md-table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  computed: {
    ...mapState(['salesByProducts'])
  },
  methods: {
    ...mapActions(['getSalesByProducts'])
  },
  created () {
    this.getSalesByProducts()
  },
  updated () {
    console.log(this.salesByProducts)
  }
}
</script>
