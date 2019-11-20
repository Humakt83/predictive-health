import Vue from 'vue'
import Vuex from 'vuex'
import {getPrediction, getPoll, getUsers} from '@/api/api';

Vue.use(Vuex)

const POLL_ANSWER_MAP = ['Never', 'Monthly', 'Weekly', 'Daily'];

const convertToSmiley = (val) => val ? '😃' : '💀';

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
      state.poll = poll.answers.map((answer) => {
        return {name: answer.name, optionValue: POLL_ANSWER_MAP[answer.optionValue - 1]}
      });
    },
    setUsers(state, users) {
      state.users = users.map(user => JSON.parse(user)).reverse();
    }
  },
  actions: {
    getPrediction: async (context, userId) => {
      const result = await getPrediction(userId);
      const prediction = [
        {name: 'Type 2 Diabetes', probability: convertToSmiley(result.data.t2d)},
        {name: 'IBD', probability: convertToSmiley(result.data.ibd)},
        {name: 'Hearth Attack', probability: convertToSmiley(result.data.ha)},
        {name: 'Prostate Cancer', probability: convertToSmiley(result.data.pc)},
        {name: 'Colorectal Cancer', probability: convertToSmiley(result.data.cc)}
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
