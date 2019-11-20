<template>
  <div class="answer-container" v-show="poll">
    <h2>ANSWERS</h2>
    <p v-for="answer in poll" :key="answer.name">
      <span class="answer-name">{{ answer.name }}: </span>
      <span>{{ answer.optionValue }}</span>
    </p>
  </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'answers',
  computed: {
    ...mapState(['poll'])
  }
}
</script>

<style scoped lang="scss">

@import "../_variables.scss";

.answer-container {
  justify-self: start;
  padding-left: 3rem;
  text-align: left;
  border-left: 3px solid $color;
  .answer-name {
    font-weight: bolder;
  }
}

</style>