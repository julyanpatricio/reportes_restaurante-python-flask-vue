<template>
  <div v-if="sales">
    <h1>ventas</h1>
    <md-table>
      <md-table-row>
        <md-table-head>factura</md-table-head>
        <md-table-head>Productos</md-table-head>
        <md-table-head>Fecha</md-table-head>
        <md-table-head>Pago</md-table-head>
        <md-table-head>Mesero</md-table-head>
      </md-table-row>

      <md-table-row v-for="(data, i) in sales" :key="i">
        <md-table-cell>{{ data.id }}</md-table-cell>
        <md-table-cell>{{
          data.products
            .map((e) => e.name)
            .reduce((unique, item) => unique.includes(item) ? unique : [...unique, item],[])
          }}</md-table-cell>
        <md-table-cell>{{ data.date_closed }}</md-table-cell>
        <md-table-cell>{{ data.total }}</md-table-cell>
        <md-table-cell>{{ data.waiter }}</md-table-cell>
      </md-table-row>
    </md-table>
    <button @click="getSales(currentPage-1); currentPage--" :disabled="currentPage===1"> < </button>
    <button @click="getSales(currentPage+1); currentPage++" :disabled="currentPage+1 ===totalSales/10"> > </button>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data: () => {
    return {
      currentPage : 1
    }
  },
  computed: {
    ...mapState(["sales","totalSales"]),
  },
  methods: {
    ...mapActions(["getSales"])
  },
  created() {
    this.getSales(1);
  },
};
</script>
