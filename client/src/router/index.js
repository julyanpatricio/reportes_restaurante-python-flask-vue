import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/views/Home'
import sales from '@/components/views/Sales'
import categories from '@/components/views/Categories'
import products from '@/components/views/Products'
import waiters from '@/components/views/Waiters'

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
      name: 'sales',
      component: sales
    },
    {
      path: '/ventas/categorias',
      name: 'categories',
      component: categories
    },
    {
      path: '/ventas/productos',
      name: 'products',
      component: products
    },
    {
      path: '/ventas/meseros',
      name: 'waiters',
      component: waiters
    }
  ]
})
