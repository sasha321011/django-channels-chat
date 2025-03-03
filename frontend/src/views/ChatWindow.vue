<template>
  <div>
    <!-- Header -->
    <div class="header">
      <div class="logo">ChatApp</div>
      <div class="nav-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
        <router-link to="/register" class="nav-link">Register</router-link>
      </div>
    </div>

    <!-- Main content: Chat and Sidebar -->
    <div class="chat-container">
      <!-- Sidebar -->
      <div class="sidebar">
        <div class="chatters">
          <div
            class="chatter"
            v-for="chatter in chatters"
            :key="chatter.id"
            @click="goToUserChat(chatter.id)"
          >
            {{ chatter.email }} (First name:{{ chatter.first_name }} Last name:{{ chatter.last_name }})
          </div>
        </div>
      </div>

      <!-- Chat Window -->
      <div class="chat-window">
        <div class="messages">
          <div
            class="message"
            v-for="msg in messages"
            :key="msg.id"
            :class="{'my-message': msg.sender === 'You', 'other-message': msg.sender !== 'You'}"
          >
            <strong>{{ msg.sender }}:</strong> {{ msg.text }}
          </div>
        </div>
        <div class="message-input">
          <input v-model="newMessage" placeholder="Type a message..." @keyup.enter="sendMessage" />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import VueCookies from 'vue-cookies';

export default {
  name: 'ChatWindow',
  data() {
    return {
      newMessage: '',
      messages: [
        { id: 1, sender: 'John Doe', text: 'Hey, how are you?' },
        { id: 2, sender: 'Jane Smith', text: 'I am good, thanks!' },
        { id: 3, sender: 'Bob Johnson', text: 'Hello everyone!' },
      ],
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

    // Отправка сообщения (заглушка)
    sendMessage() {
      if (this.newMessage.trim()) {
        const newMsg = {
          id: this.messages.length + 1, // Просто увеличиваем ID
          sender: 'You', // Отправитель — текущий пользователь
          text: this.newMessage, // Текст сообщения
        };
        this.messages.push(newMsg); // Добавляем сообщение в список
        this.newMessage = ''; // Очищаем поле ввода

        // Заглушка для WebSocket (позже замените на реальный вызов)
        console.log('Сообщение отправлено (заглушка):', newMsg);
      }
    },

    // Переход к чату с пользователем
    goToUserChat(userId) {
      this.$router.push(`/chat/${userId}`);
    },
  },
};
</script>

<style scoped>
/* Header styles */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #2f3b65;
  color: #fff;
}

.header .logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-links {
  display: flex;
}

.nav-link {
  margin-left: 20px;
  text-decoration: none;
  color: #fff;
  font-weight: bold;
}

.nav-link:hover {
  color: #42b983;
}

.chat-container {
  display: flex;
  height: calc(100vh - 60px); /* Adjusted to account for header height */
}

.sidebar {
  width: 250px;
  background-color: #2f3b52;
  color: #fff;
  padding: 20px;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.chatters {
  margin-top: 20px;
}

.chatter {
  margin-bottom: 10px;
  font-size: 16px;
  cursor: pointer;
}

.chatter:hover {
  background-color: #3c4b64;
  padding: 5px;
  border-radius: 4px;
}

.chat-window {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 20px;
}

.message {
  margin-bottom: 10px;
  font-size: 16px;
}

.my-message {
  text-align: left;
  background-color: #e1f5fe;
  padding: 10px;
  border-radius: 8px;
  margin-left: 0;
  margin-right: auto;
}

.other-message {
  text-align: right;
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 8px;
  margin-left: auto;
  margin-right: 0;
}

.message-input {
  display: flex;
  gap: 10px;
}

.message-input input {
  width: 80%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.message-input button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.message-input button:hover {
  background-color: #45a049;
}
</style>