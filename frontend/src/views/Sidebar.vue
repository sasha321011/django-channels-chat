<template>
  <div class="sidebar">
    <div class="chatters">
      <div class="chatter" v-for="chatter in chatters" :key="chatter.id">
        {{ chatter.name }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sidebar',
  data() {
    return {
      chatters: [
        { id: 1, name: 'John Doe' },
        { id: 2, name: 'Jane Smith' },
        { id: 3, name: 'Bob Johnson' }
      ]
    }
  }
}
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
