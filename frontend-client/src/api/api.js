import * as axios from 'axios';

const BASE_HREF="http://localhost:5000/";

const postAnswers = (userId, answerData) => {
  return axios.post(`${BASE_HREF}user/${userId}/poll`, answerData);
}

const createUser = () => {
  return axios.post(`${BASE_HREF}user`, {});
}

export {
  postAnswers,
  createUser
};
