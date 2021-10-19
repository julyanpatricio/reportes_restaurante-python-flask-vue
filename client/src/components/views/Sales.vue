<template>
  <div v-if="sales">
    <h1>ventas</h1>
    <ul>
      <li v-for="(sale, i) in sales" :key="i">
        id: {{ sale.id }} - total: {{ sale.total }} - date {{ sale.date_closed }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  // data: () => ({
  //   ventas: null
  // }),
  computed: {
    ...mapState(['sales'])
  },
  methods: {
    ...mapActions(['getSales'])
  },
  created () {
    this.getSales()
  }
}
</script>
