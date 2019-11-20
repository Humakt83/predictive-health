<template>
  <div class="home">
    <h1>HEALTH PREDICTION</h1>
    <div class="container">
      <users />
      <prediction-results />
    </div>
  </div>
</template>

<script>
import PredictionResults from '@/components/PredictionResults';
import Users from '@/components/Users';

export default {
  name: 'home',
  components: {
    PredictionResults,
    Users,
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
  created() {
    this.$store.dispatch('getUsers');
  },
}
</script>
<style scoped lang="scss">
@import '../_variables.scss';

.home {
  margin-top: 45vh;
  .container {
    display: grid;
    grid-template-columns: 30vw auto;
  }
  
  h1 {
    color: $color;
  }
}

</style>
