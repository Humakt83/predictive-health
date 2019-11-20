<template>
  <div class="section-container" v-show="prediction">
    <h2>PREDICTION</h2>
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

.section-container {
  justify-self: start;
  padding-left: 3rem;
  text-align: left;
  border-left: 3px solid $color;
}

</style>