<template>
  <div v-if="salesByCategories">
    <h1>ventas por categorias</h1>
    <md-table>
      <md-table-row>
        <md-table-head>Categoria</md-table-head>
        <md-table-head>Cantidades vendidas</md-table-head>
        <md-table-head>Ingresos Totales</md-table-head>
      </md-table-row>

      <md-table-row  v-for="(value, key) in salesByCategories" :key="key">
        <md-table-cell>{{key}}</md-table-cell>
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
    ...mapState(['salesByCategories', 'dateMinSelected', 'dateMaxSelected'])
  },
  methods: {
    ...mapActions(['getSalesByCategories'])
  },
  created () {
    this.getSalesByCategories({dateStart: this.dateMinSelected, dateEnd: this.dateMaxSelected})
  },
  watch: {
    dateMinSelected: function (newData, oldData) {
      if (newData !== oldData) {
        this.getSalesByCategories({dateStart: this.dateMinSelected, dateEnd: this.dateMaxSelected})
      }
    },
    dateMaxSelected: function (newData, oldData) {
      if (newData !== oldData) {
        this.getSalesByCategories({dateStart: this.dateMinSelected, dateEnd: this.dateMaxSelected})
      }
    }
  }
}
</script>
