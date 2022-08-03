import axios from 'axios'


 const api = axios.create({
    withCredentials: true,
    baseURL : "http://127.0.0.1:8000/",
    headers: {'Content-Type': 'application/json'},
    credentials: 'include',
});
let refresh = false;

api.interceptors.response.use(resp => resp, async error => {
   if (error.response.status === 403 && !refresh) {
       refresh = true;
       console.log("Entered interceptors")
       const token = localStorage.getItem('jwt');
       const r_token = localStorage.getItem('r_token');
       api.defaults.headers.common['Authorization'] = `Bearer ${token}`;

       const {status, data} = await api.post('/auth/refresh', {'r_token': r_token}, {
           withCredentials: true
       });
       console.log("Entered interceptors", status)
       if (status === 200) {
           api.defaults.headers.common['Authorization'] = `Bearer ${data.token}`;

           return api(error.config);
       }
   }
   refresh = false;
   return error;
});


export default api;