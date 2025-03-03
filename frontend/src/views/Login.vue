<template>
  <div class="form-container">
    <form @submit.prevent="login">
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.password" type="password" placeholder="Password" required />
      <button type="submit">SAVE</button>
    </form>
    <p v-if="message" :class="{ success: success, error: !success }">{{ message }}</p>
    <p>Нет аккаунта? <button @click="goToRegister" class="link-button">Регистрация</button></p>
  </div>
</template>

<script>
import axios from 'axios';
import VueCookies from 'vue-cookies';

export default {
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      message: '',
      success: false
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('accs/login/', this.form);
        if (response.status === 201 || response.status === 200) {
          this.message = 'Login successful!';
          this.success = true;

          // Сохраняем токен в куки
          const token = response.data.token;
          VueCookies.set('token', token, '1d'); // Токен сохраняется на 1 день

          setTimeout(() => {
            this.$router.push('/');
          }, 1000);
        }
      } catch (error) {
        this.message = error.response?.data?.message || 'Login failed!';
        this.success = false;
      }
    },
    goToRegister() {
      this.$router.push('/register');
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