import Vue from 'vue'
import Vuex from 'vuex'
import getPrediction from '@/api/prediction';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    prediction: undefined
  },
  mutations: {
    setPrediction(state, prediction) {
      state.prediction = prediction;
    }
  },
  actions: {
    getPrediction: async (context, userId) => {
      if (!userId) {
        await getPrediction(userId);
      }
      const prediction = [
        {name: 'Type 2 Diabetes', probability: 20},
        {name: 'IBD', probability: 30},
        {name: 'Hearth Attack', probability: 50},
        {name: 'Prostate Cancer', probability: 75},
        {name: 'Colorectal Cancer', probability: 60}
      ];
      context.commit('setPrediction', prediction);
    }
  },
})
