<template>
  <div class="home">
    <h1>HEALTH PREDICTIVE QUESTIONAIRE</h1>
    <answer-option v-for="section in sections" :section="section" :key="section.name" @optionSelected="selectOption"/>
    <div class="submit">
      <button @click="submit" :disabled="submitDisabled">SUBMIT</button>
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
        {name: 'Milk/Cheese', image: 'milk.png'},
        {name: 'Yoghurt/Kefir', image: 'milk.png'},
        {name: 'Red/Processed Meat', image: 'beefmeat.png'},
        {name: 'Tea/Coffee', image: 'coffeecup.png'},
        {name: 'Sweetened Beverages', image: 'milk.png'},
        {name: 'Fruits', image: 'milk.png'},
        {name: 'Vegetables', image: 'broccoli.png'},
        {name: 'Whole-grain', image: 'milk.png'},
        {name: 'Fish', image: 'milk.png'},
        {name: 'Refined Cereals', image: 'milk.png'},
        {name: 'Poultry', image: 'milk.png'},
        {name: 'Legumes', image: 'milk.png'},
        {name: 'Nuts/Seeds', image: 'milk.png'},
        {name: 'Eggs', image: 'milk.png'}
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
  line-height: 54px;
  font-family: Roboto;
  font-size: 32px;
}

.submit {
  button {
    border-radius: 100px;
    background-color: $color2;
    font-family: Montserrat;
    font-weight: bold;
    font-size: 26px;
    padding: 25px 75px;
    color: $color-background;
    border: none;
    cursor: pointer;
    &:disabled {
      cursor: not-allowed;
      background-color: $color3;
    }
  }
}

</style>
