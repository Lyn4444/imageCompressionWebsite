import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import Forget from "@/components/Forget.vue";
import HomeImage from "@/components/HomeImage.vue";
import About from "@/components/About.vue";
import Info from "@/components/info.vue";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/forget',
      name: Forget,
      component: Forget
    },
    {
      path: '/home-image',
      name: HomeImage,
      component: HomeImage
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/info',
      name: 'Info',
      component: Info
    },
  ]
})
