import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FindFlights from '../views/FindFlights.vue'
import ReservationForm from '../views/ReservationForm.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/find-flights',
      name: 'findFlights',
      component: FindFlights
    },
    {
      path: '/reserve/:id',
      name: 'reserve',
      component: ReservationForm,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})

export default router