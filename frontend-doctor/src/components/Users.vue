<template>
  <div class="users">
    <div class="users-header">
      <h2>USERS</h2>
      <font-awesome-icon class="sync" icon="sync" @click="getUsers"/>
    </div>
    <ol type="none">
      <li class="user" :class="{'selected': user._id === selectedUser}" v-for="user in users" :key="user._id" @click="getPrediction($event, user._id)">
        {{ user._id }}
      </li>
    </ol>
  </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'users',
  data: () => {
    return {
      selectedUser: undefined
    }
  },
  computed: {
    ...mapState(['users'])
  },
  methods: {
    getPrediction(event, userId) {
      event.preventDefault();
      this.selectedUser = userId;
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
  .users-header {
    display: flex;
    justify-content: space-evenly;
    align-items: baseline;
    .sync {
      cursor: pointer;
      background: $color3;
      border-radius: 100px;
      padding: 4px;
      &:hover {
        background: $color4;
      }
    }
  }
  .user {
    font-weight: bolder;
    cursor: pointer;
    line-height: 1.7;
    +.selected,
    &:hover {
      color: $color2;
    }
  }
}
</style>