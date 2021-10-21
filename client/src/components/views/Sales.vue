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
            .reduce(
              (unique, item) =>
                unique.includes(item) ? unique : [...unique, item],
              []
            )
        }}</md-table-cell>
        <md-table-cell>{{ data.date_closed }}</md-table-cell>
        <md-table-cell>{{ data.total }}</md-table-cell>
        <md-table-cell>{{ data.waiter }}</md-table-cell>
      </md-table-row>
    </md-table>
    <button @click="currentPage = 1" :disabled="currentPage === 1">
      First Page
    </button>
    <button @click="currentPage--" :disabled="currentPage === 1">
      Prev Page
    </button>
    <button @click="currentPage++" :disabled="currentPage + 1 === Math.ceil(totalSales / 10)">
      Next Page
    </button>
    <button @click="currentPage = Math.ceil(totalSales / 10) - 1" :disabled="currentPage + 1 === Math.ceil(totalSales / 10)">
      End Page
    </button>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import format from "date-fns/format";

export default {
  data: () => {

    return {
      currentPage: 1,
    };
  },
  computed: {
    ...mapState(["sales", "totalSales", "dateMinSelected", "dateMaxSelected"]),
  },
  methods: {
    ...mapActions(["getSales"]),
    filterByDate() {
      this.getSales({
        page: 1,
        dateStart: this.dateMinSelected,
        dateEnd: this.dateMaxSelected,
      });
      this.currentPage = 1;
    },
    changePage() {
      this.getSales({
        page: this.currentPage,
        dateStart: this.dateMinSelected,
        dateEnd: this.dateMaxSelected,
      });
    },
  },
  created() {
    this.getSales({ page: 1 });
  },
  watch: {
    dateMinSelected: function (newData,oldData) {
      if(newData!==oldData){
      this.filterByDate()
      }
    },
    dateMaxSelected: function (newData,oldData) {
      if(newData!==oldData){
      this.filterByDate()
      }
    },
    currentPage: function () {
      this.changePage();
    },
  },
};
</script>

<style scoped>
.container-dataPicker {
  display: flex;
  padding-inline: 30%;
  align-items: center;
}
</style>