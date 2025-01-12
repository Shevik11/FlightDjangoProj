<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/find-flights">Find Flights</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
/* Add your global styles here */
.form-group {
  margin-bottom: 1rem;
}

.form-group input {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

.btn {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  display: inline-block;
  margin: 0.5rem;
}

.flight-card {
  border: 1px solid #ddd;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 4px;
}

nav {
  padding: 1rem;
  background-color: #f8f9fa;
}

nav a {
  margin: 0 0.5rem;
  text-decoration: none;
  color: #333;
}

nav a.router-link-active {
  color: #4CAF50;
}
</style>