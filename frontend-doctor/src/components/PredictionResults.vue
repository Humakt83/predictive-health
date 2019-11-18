<template>
  <div class="section-container" v-show="prediction">
    <p v-for="disease in prediction" :key="disease.name">
      {{ disease.name }} {{ disease.probability}} %
    </p>
    <p>
      {{ JSON.stringify(poll) }}
    </p>
  </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'prediction-results',
  computed: {
    ...mapState(['prediction', 'poll'])
  }
}
</script>

<style scoped lang="scss">

@import "../_variables.scss";

</style>