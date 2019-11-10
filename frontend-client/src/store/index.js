import Vue from 'vue'
import Vuex from 'vuex'
import postAnswers from '@/api/answers';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    answersPosted: false
  },
  mutations: {
    setAnswersToPosted(state) {
      state.answersPosted = true;
    }
  },
  actions: {
    submitAnswers: async (context, answerData) => {
      await postAnswers(answerData);
      context.commit('setAnswersToPosted');
    }
  },
})
