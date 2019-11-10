<template>
  <div class="home">
    <h1>PREDICTIVE HEALTH</h1>
    <answer-option v-for="section in sections" :section="section" :key="section"/>
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
    }
  }
}
</script>
