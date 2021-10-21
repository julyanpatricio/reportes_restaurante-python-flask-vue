<template>
  <div id="app">
    <app-header></app-header>
    <filters v-if="currentRoutePath !== '/'"></filters>
    <router-view class='container' />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import AppHeader from './components/AppHeader'
import Filters from './components/Filters'

export default {
  name: 'App',
  components: { AppHeader,Filters },
  computed: {
    currentRoutePath() {
        return this.$route.path
    }
  },
  methods: {
    ...mapActions(["getDateMinAndDateMax"])
  },
  created() {
    this.getDateMinAndDateMax()
  }
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
