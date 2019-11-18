<template>
  <div class="home">
    <h1>PREDICTIVE HEALTH - DOCTOR CLIENT</h1>
    <form v-on:submit.prevent @submit="getPrediction($event)">
      <label for="userInput">User Id</label>
      <input name="userInput" type="text" placeholder="Insert User Id here" v-model="userId" />
      <input type="submit" :disabled="submitDisabled" text="Get Prediction"/>
    </form>
    <prediction-results />
  </div>
</template>

<script>
import PredictionResults from '@/components/PredictionResults';

export default {
  name: 'home',
  components: {
    PredictionResults
  },
  data: () => {
    return {
      userId: undefined
    }
  },
  computed: {
    submitDisabled() {
      return !this.userId || this.userId.trim().length < 1;
    }
  },
  methods: {
    getPrediction(event) {
      event.preventDefault();
      this.$store.dispatch('getPrediction', this.userId);
      this.$store.dispatch('getPoll', this.userId);
    },
  }
}
</script>
<style scoped lang="scss">
@import '../_variables.scss';

h1 {
  color: $color;
}

</style>
