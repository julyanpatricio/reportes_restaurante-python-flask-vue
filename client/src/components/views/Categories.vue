<template>
  <div v-if="salesByCategories">
    <h1>ventas</h1>
    <ul>
      <li v-for="(value, key) in salesByCategories" :key="key">
        categoria: {{ key }}
        cantidades vendidas: {{ value['total quantities'] }}
        ingresos totales: {{ value['total incomes'] }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  computed: {
    ...mapState(['salesByCategories'])
  },
  methods: {
    ...mapActions(['getSalesByCategories'])
  },
  created () {
    this.getSalesByCategories()
  },
  updated () {
    console.log(this.salesByCategories)
  }
}
</script>
