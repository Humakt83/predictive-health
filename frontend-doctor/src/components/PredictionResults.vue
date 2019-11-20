<template>
  <div class="section-container" v-show="prediction">
    <h2>PREDICTION</h2>
    <div class="disease" v-for="disease in prediction" :key="disease.name">
      <div class="disease-name">
        {{ disease.name }}
      </div>
      <div class="disease-value">
        {{ disease.probability }}
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'prediction-results',
  computed: {
    ...mapState(['prediction'])
  }
}
</script>

<style scoped lang="scss">

@import "../_variables.scss";

.section-container {
  padding-left: 3rem;
  text-align: center;
  border-left: 3px solid $color;
  .disease {
    font-family: Roboto;
    color: $color4;
    border-radius: 15px;
    background-color: $color;
    padding: 8px 12px;
    font-size: 24px;
    margin: auto;
    margin-bottom: 15px;
    width: 400px;
    .disease-name {
      font-weight: 600;
      display: inline;
    }
    .disease-value {
      display: inline;
      font-weight: 800;
      margin-left: 2rem;
    }
  }
}

</style>