import Vue from 'vue'
import Vuex from 'vuex'
import {getPrediction, getPoll, getUsers} from '@/api/api';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    prediction: undefined,
    poll: undefined,
    users: []
  },
  mutations: {
    setPrediction(state, prediction) {
      state.prediction = prediction;
    },
    setPollAnswers(state, poll) {
      state.poll = poll;
    },
    setUsers(state, users) {
      state.users = users.map(user => JSON.parse(user));
    }
  },
  actions: {
    getPrediction: async (context, userId) => {
      const result = await getPrediction(userId);
      const prediction = [
        {name: 'Type 2 Diabetes', probability: result.data.t2d},
        {name: 'IBD', probability: result.data.ibd},
        {name: 'Hearth Attack', probability: result.data.ha},
        {name: 'Prostate Cancer', probability: result.data.pc},
        {name: 'Colorectal Cancer', probability: result.data.cc}
      ];
      context.commit('setPrediction', prediction);
    },
    getPoll: async (context, userId) => {
      const poll = await getPoll(userId);
      context.commit('setPollAnswers', poll.data);
    },
    getUsers: async(context) => {
      const result = await getUsers();
      context.commit('setUsers', result.data);
    }
  },
})
