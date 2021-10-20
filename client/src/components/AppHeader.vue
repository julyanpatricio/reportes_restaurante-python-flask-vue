<template>
  <header>
    <span class="title">La pikada de la esquina</span>
    <router-link to="/" class="btn-header"> home </router-link>
    <select name="rutas" id="rutas" v-on:click="redirectTo">
      <option value="/">home</option>
      <option value="/ventas">ventas generales</option>
      <option value="/ventas/categorias">ventas por categorias</option>
      <option value="/ventas/productos">ventas por productos</option>
      <option value="/ventas/meseros">ventas por meseros</option>
    </select>
  </header>
</template>

<script>
import router from '@/router'
export default {
  name: 'app-header',
  methods: {
    redirectTo: (e) => router.push(e.target.value)
  }
}
</script>

<style scoped>
header {
  display: block;
  height: 8%;
  background-color: black;
  color: aliceblue;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: x-large;
  padding-inline: 2%;
}
</style>
