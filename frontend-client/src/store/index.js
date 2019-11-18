import Vue from 'vue'
import Vuex from 'vuex'
import {postAnswers, createUser} from '@/api/api';

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
      const transformedAnswerData = answerData.map((answer) => {
        const convertOptions = {Daily: 4, Weekly: 3, Monthly: 2, Never: 1};
        return { name: answer.name, optionValue: convertOptions[answer.optionValue]};
      });
      const response = await createUser();
      const userId = response.data._id;
      await postAnswers(response.data._id, {user: userId, answers: transformedAnswerData});
      context.commit('setAnswersToPosted');
    }
  },
})
