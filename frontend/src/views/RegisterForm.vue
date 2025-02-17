<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4 w-50">
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <input v-model="form.email" type="email" class="form-control" placeholder="Email" required>
        </div>
        <div class="mb-3">
          <input v-model="form.first_name" type="text" class="form-control" placeholder="First Name" required>
        </div>
        <div class="mb-3">
          <input v-model="form.last_name" type="text" class="form-control" placeholder="Last Name" required>
        </div>
        <div class="mb-3">
          <input v-model="form.password" type="password" class="form-control" placeholder="Password" required>
        </div>
        <button type="submit" class="btn btn-primary w-100">SAVE</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        first_name: '',
        last_name: '',
        password: '',
      }
    };
  },
  methods: {
    submitForm() {
      console.log('Форма отправлена', this.form);
      // Тут можно добавить запрос на API через Axios
    }
  }
};
</script>

<style>
.card {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}
</style>
