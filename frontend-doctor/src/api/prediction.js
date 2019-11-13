import * as axios from 'axios';

const getPrediction = (user) => {
  return axios.get(`/user/${user}/prediction`);
}

export default getPrediction;
