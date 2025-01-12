<script>
import axios from 'axios'

export default {
  name: 'ReservationForm',
  props: ['id'],
  data() {
    return {
      passenger: {
        firstName: '',
        lastName: '',
        email: '',
        phoneNumber: '',
        id: this.id
      }
    }
  },
  methods: {
    async saveReservation() {
      try {
        await axios.post('http://localhost:8000/flightservices/saveReservation/', this.passenger)
        alert('Reservation saved successfully!')
        this.$router.push('/')
      } catch (error) {
        console.error('Error saving reservation:', error)
        alert('Error saving reservation')
      }
    }
  }
}
</script>

<template>
  <div class="reservation-form">
    <h2>Make Reservation</h2>
    <form @submit.prevent="saveReservation">
      <div class="form-group">
        <input v-model="passenger.firstName" placeholder="First Name" required>
      </div>
      <div class="form-group">
        <input v-model="passenger.lastName" placeholder="Last Name" required>
      </div>
      <div class="form-group">
        <input type="email" v-model="passenger.email" placeholder="Email" required>
      </div>
      <div class="form-group">
        <input v-model="passenger.phoneNumber" placeholder="Phone Number" required>
      </div>
      <button type="submit">Reserve Flight</button>
    </form>
  </div>
</template>

<style scoped>

</style>