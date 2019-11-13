import * as axios from 'axios';

const BASE_HREF="http://localhost:5000/";

const getPrediction = (user) => {
  return axios.get(`${BASE_HREF}user/${user}/prediction`);
}

const getPoll = (user) => {
  return axios.get(`${BASE_HREF}user/${user}/poll`);
}

export {
  getPrediction,
  getPoll
}
