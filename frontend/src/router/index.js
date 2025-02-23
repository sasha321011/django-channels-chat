import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '../views/RegisterForm.vue'
import Login from '../views/Login.vue'
import ChatWindow from '../views/ChatWindow.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
    {
    path: '/register',
    name: 'register',
    component: RegisterForm
  },
    {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/chats',
    name: 'chats',
    component: ChatWindow
  },

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
