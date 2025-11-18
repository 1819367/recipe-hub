import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.PROD ? '/api' : '/api', //both work thanks to proxy or same domain in prod
})

export default api;