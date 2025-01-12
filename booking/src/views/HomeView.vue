<script>
export default {
  name: 'HomeView',
  data() {
    return {
      isLoggedIn: false
    }
  },
  created() {
    this.isLoggedIn = !!localStorage.getItem('token')
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.isLoggedIn = false
    }
  }
}
</script>

<template>
  <div class="home">
    <h1>Welcome to Flight Booking System</h1>
    <router-link to="/find-flights" class="btn">Find Flights</router-link>
    <router-link v-if="!isLoggedIn" to="/login" class="btn">Login</router-link>
    <button v-else @click="logout" class="btn">Logout</button>
  </div>
</template>

<style scoped>

</style>