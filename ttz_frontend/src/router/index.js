import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/login.vue'


function guardMyroute(to, from, next){
  var isAuthenticated= false; 
  if(localStorage.getItem('email') != null){
    isAuthenticated = true;
  }
  else{
    isAuthenticated= false;
  }
    
  if(isAuthenticated) 
  {
    next();
  } 
  else
  {
    next('/');
  }
}

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login,
    // beforeEnter : guardMyroute,
    
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "about" */ '../views/register.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
