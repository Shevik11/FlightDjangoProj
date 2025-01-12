<script>
import axios from 'axios'

export default {
  name: 'FindFlights',
  data() {
    return {
      search: {
        departureCity: '',
        arrivalCity: '',
        dateOfDeparture: ''
      },
      flights: []
    }
  },
  methods: {
    async searchFlights() {
      try {
        const response = await axios.post('http://localhost:8000/flightservices/findFlights/', this.search)
        this.flights = response.data
      } catch (error) {
        console.error('Error finding flights:', error)
      }
    }
  }
}
</script>

<template>
  <div class="find-flights">
    <h2>Find Flights</h2>
    <form @submit.prevent="searchFlights">
      <div class="form-group">
        <input v-model="search.departureCity" placeholder="Departure City" required>
      </div>
      <div class="form-group">
        <input v-model="search.arrivalCity" placeholder="Arrival City" required>
      </div>
      <div class="form-group">
        <input type="date" v-model="search.dateOfDeparture" required>
      </div>
      <button type="submit">Search</button>
    </form>

    <div v-if="flights.length" class="flights-list">
      <div v-for="flight in flights" :key="flight.id" class="flight-card">
        <h3>{{ flight.operatingAirlines }} - {{ flight.flightNumber }}</h3>
        <p>From: {{ flight.departureCity }} To: {{ flight.arrivalCity }}</p>
        <p>Date: {{ flight.dateOfDeparture }}</p>
        <p>Time: {{ flight.estimatedTimeOfDeparture }}</p>
        <router-link :to="'/reserve/' + flight.id" class="btn">Reserve</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>