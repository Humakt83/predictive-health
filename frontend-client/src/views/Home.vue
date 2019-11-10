<template>
  <div class="home">
    <h1>PREDICTIVE HEALTH</h1>
    <answer-option v-for="section in sections" :section="section" :key="section" @optionSelected="selectOption"/>
    <div class="submit">
      <button @click="submit" :disabled="submitDisabled">Submit</button>
      <p v-if="submitDisabled && !answersPosted">Select all the sections before pressing submit</p>
      <p v-if="answersPosted">You have successfully sent the answers.</p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import AnswerOption from '@/components/AnswerOption.vue'
import { mapState } from 'vuex';

export default {
  name: 'home',
  components: {
    AnswerOption
  },
  data: () => {
    return {
      sections: [
        'Milk/Cheese',
        'Yoghurt/Kefir (fermented milk products)',
        'Red/Processed Meat',
        'Tea/Coffee',
        'Sweetened Beverages',
        'Fruits',
        'Vegetables',
        'Whole-grain',
        'Fish',
        'Refined Cereals',
        'Poultry',
        'Legumes',
        'Nuts/Seeds',
        'Eggs',
      ],
      answers: []
    }
  },
  computed: {
    submitDisabled() {
      return this.answers.length < this.sections.length || this.answersPosted;
    },
    ...mapState(['answersPosted'])
  },
  methods: {
    submit() {
      this.$store.dispatch('submitAnswers', this.answers);
    },
    selectOption(name, optionValue) {
      this.answers = this.answers.filter((answer) => answer.name !== name);
      this.answers.push({name, optionValue});
    }
  }
}
</script>
<style scoped lang="scss">
@import '../_variables.scss';

h1 {
  color: $color;
}

</style>
