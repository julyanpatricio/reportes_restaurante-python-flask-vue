import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/views/Home'
import ventas from '@/components/views/Ventas'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/ventas',
      name: 'ventas',
      component: ventas
    }
  ]
})
