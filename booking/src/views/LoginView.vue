<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api-auth/', this.credentials)
        localStorage.setItem('token', response.data.token)
        this.$router.push('/')
      } catch (error) {
        console.error('Login error:', error)
        alert('Login failed')
      }
    }
  }
}
</script>

<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <input v-model="credentials.username" placeholder="Username" required>
      </div>
      <div class="form-group">
        <input type="password" v-model="credentials.password" placeholder="Password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<style scoped>

</style>