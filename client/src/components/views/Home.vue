<template>
  <div>
    <h1>Home</h1>
    <router-link :to="{ name: 'ventas' }">
      <span>ventas</span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'home-view'
}
</script>
