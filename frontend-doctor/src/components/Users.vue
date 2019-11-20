<template>
  <div class="users">
    <h2>USERS</h2>
    <button @click="getUsers">Refresh</button>
    <p v-for="user in users" :key="user._id" @click="getPrediction($event, user._id)">
      {{ user._id }}
    </p>
  </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'users',
  computed: {
    ...mapState(['users'])
  },
  methods: {
    getPrediction(event, userId) {
      event.preventDefault();
      this.$store.dispatch('getPrediction', userId);
      this.$store.dispatch('getPoll', userId);
    },
    getUsers() {
      this.$store.dispatch('getUsers');
    }
  }
}
</script>

<style scoped lang="scss">

@import "../_variables.scss";

.users {
  justify-self: end;
  padding-right: 3rem;
}
</style>