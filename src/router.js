import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
import Pos from './views/Pos.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'pos',
      component: Pos,
    },
    {
      path: '/other',
      name: 'Other',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Other.vue')
    },
    {
      path: '/home',
      name: 'pos',
      component: () => import(/* webpackChunkName: "about" */ './views/Pos.vue')
    },


  ]
})
