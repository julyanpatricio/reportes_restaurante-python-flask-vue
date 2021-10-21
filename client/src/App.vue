<template>
  <div id="app">
    <app-header></app-header>
    <filters></filters>
    <router-view class='container' />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader'
import Filters from './components/Filters'

export default {
  name: 'App',
  components: { AppHeader,Filters }
}
</script>

<style>
html, body, #app{
  height: -webkit-fill-available;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  margin: 0;
}

.md-table-head {
  text-align: center;
}
</style>
