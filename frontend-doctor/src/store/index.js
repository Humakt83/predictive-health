import Vue from 'vue'
import Vuex from 'vuex'
import {getPrediction, getPoll} from '@/api/api';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    prediction: undefined,
    poll: undefined
  },
  mutations: {
    setPrediction(state, prediction) {
      state.prediction = prediction;
    },
    setPollAnswers(state, poll) {
      state.poll = poll;
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
    },
    getPoll: async (context, userId) => {
      const poll = await getPoll(userId);
      context.commit('setPollAnswers', poll.data);
    }
  },
})
