import * as axios from 'axios';

const postAnswers = (answerData) => {
  return axios.post('/food', answerData);
}

export default postAnswers;
