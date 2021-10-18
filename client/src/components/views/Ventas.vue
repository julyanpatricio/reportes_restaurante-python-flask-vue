<template>
  <div v-if="ventas">
    <h1>ventas</h1>
    <ul>
      <li v-for="(venta, i) in ventas" :key="i">
        id: {{ venta.id }} - total: {{ venta.total }}
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
    ...mapState(['ventas'])
  },
  methods: {
    ...mapActions(['getVentas'])
  },
  created () {
    this.getVentas()
  }
}
</script>
