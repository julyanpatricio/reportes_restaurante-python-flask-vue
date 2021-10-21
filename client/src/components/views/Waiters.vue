<template>
  <div v-if="salesByWaiters">
    <h1>ventas por meseros</h1>
    <md-table>
      <md-table-row>
        <md-table-head>Mesero</md-table-head>
        <md-table-head>Productos vendidos</md-table-head>
        <md-table-head>Total recaudado</md-table-head>
      </md-table-row>

      <md-table-row  v-for="(value, key) in salesByWaiters" :key="key">
        <md-table-cell>{{key}}</md-table-cell>
        <md-table-cell>{{ value['saled products'] }}</md-table-cell>
        <md-table-cell>{{ value['total income for sales'] }}</md-table-cell>
      </md-table-row>

    </md-table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  computed: {
    ...mapState(['salesByWaiters','dateMinSelected','dateMaxSelected'])
  },
  methods: {
    ...mapActions(['getSalesByWaiters'])
  },
  created () {
    this.getSalesByWaiters({dateStart:this.dateMinSelected,dateEnd:this.dateMaxSelected})
  },
  watch: {
    dateMinSelected: function (newData,oldData) {
      if(newData!==oldData){
        this.getSalesByWaiters({dateStart:this.dateMinSelected,dateEnd:this.dateMaxSelected})
      }
    },
    dateMaxSelected: function (newData,oldData) {
      if(newData!==oldData){
        this.getSalesByWaiters({dateStart:this.dateMinSelected,dateEnd:this.dateMaxSelected})
      }
    }
  }
}
</script>
