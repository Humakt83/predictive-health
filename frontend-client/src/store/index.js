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
        const convertOptions = {Daily: 1, Weekly: 2, Monthly: 3, Never: 4};
        return { name: answer.name, optionValue: convertOptions[answer.optionValue]};
      });
      const response = await createUser();
      const userId = response.data._id;
      await postAnswers(response.data._id, {user: userId, answers: transformedAnswerData});
      context.commit('setAnswersToPosted');
    }
  },
})
