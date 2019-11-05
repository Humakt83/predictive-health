<template>
  <div class="home">
    <h1>PREDICTIVE HEALTH</h1>
    <answer-option v-for="answerOption in answersAndOptions" :answerOption="answerOption" :key="answerOption.name"/>
  </div>
</template>

<script>
// @ is an alias to /src
import AnswerOption from '@/components/AnswerOption.vue'

export default {
  name: 'home',
  components: {
    AnswerOption
  },
  data: () => {
    return {
      answersAndOptions: [
        {
          name: 'Milk/Cheese',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
        {
          name: 'Yoghurt/Kefir (fermented milk products)',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
        {
          name: 'Red/Processed Meat',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Tea/Coffee',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Sweetened Beverages',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Fruits',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Vegetables',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Whole-grain',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Fish',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Refined Cereals',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
                {
          name: 'Poultry',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
        {
          name: 'Legumes',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
        {
          name: 'Nuts/Seeds',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
        {
          name: 'Eggs',
          options: ['Daily', 'Weekly', 'Monthly', 'Never']
        },
      ],
    }
  }
}
</script>
