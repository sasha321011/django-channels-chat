<template>
  <div class="form-container">
    <form @submit.prevent="register">
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.first_name" type="text" placeholder="First Name" required />
      <input v-model="form.last_name" type="text" placeholder="Last Name" required />
      <input v-model="form.password" type="password" placeholder="Password" required />
      <button type="submit">SAVE</button>
    </form>
    <p v-if="message" :class="{ success: success, error: !success }">{{ message }}</p>
    <p>Уже есть аккаунт? <button @click="goToLogin" class="link-button">Войти</button></p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        email: '',
        first_name: '',
        last_name: '',
        password: ''
      },
      message: '',
      success: false
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('accs/registration/', this.form);
        if (response.status === 201 || response.status === 200) {
          this.message = 'Registration successful!';
          this.success = true;
          setTimeout(() => {
            this.$router.push('/login');
          }, 1000);
        }
      } catch (error) {
        this.message = error.response?.data?.message || 'Registration failed!';
        this.success = false;
      }
    },
    goToLogin() {
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.form-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: white;
}

input {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background: blue;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.success {
  color: green;
}

.error {
  color: red;
}

.link-button {
  background: none;
  border: none;
  color: blue;
  cursor: pointer;
  text-decoration: underline;
}
</style>
