<template>
  <div>
    <h1>Home</h1>
    <router-link :to="{ name: 'sales' }">
      <span>ventas generales</span>
    </router-link>
    <router-link :to="{ name: 'categories' }">
      <span>ventas agreupadas por categorias</span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'home-view'
}
</script>
