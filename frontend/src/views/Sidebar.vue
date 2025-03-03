<template>
  <div class="sidebar">
    <div class="chatters">
      <div class="chatter" v-for="chatter in chatters" :key="chatter.id">
        {{ chatter.email }} ({{ chatter.first_name }} {{ chatter.last_name }})
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import VueCookies from 'vue-cookies';

export default {
  name: 'Sidebar',
  data() {
    return {
      chatters: [], // Список пользователей
      token: null,  // Токен из куки
    };
  },
  async created() {
    // Извлекаем токен из куки
    this.token = VueCookies.get('token');

    // Если токен есть, получаем список пользователей
    if (this.token) {
      await this.fetchChatters();
    } else {
      console.error('Токен отсутствует');
      this.$router.push('/login'); // Перенаправляем на страницу входа, если токена нет
    }
  },
  methods: {
    // Получение списка пользователей
    async fetchChatters() {
      try {
        const response = await axios.get('/api/users/', {
          headers: {
            Authorization: `Bearer ${this.token}`, // Используем токен из куки
          },
        });
        this.chatters = response.data; // Сохраняем список пользователей
      } catch (error) {
        console.error('Ошибка при загрузке пользователей:', error);
        this.$router.push('/login'); // Перенаправляем на страницу входа в случае ошибки
      }
    },
  },
};
</script>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #2f3b52;
  color: #fff;
  padding: 20px;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
}

.chatters {
  margin-top: 20px;
}

.chatter {
  margin-bottom: 10px;
  font-size: 16px;
  cursor: pointer;
}
</style>