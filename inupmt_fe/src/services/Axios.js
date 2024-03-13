import axios from "axios"

const Axios = axios.create({
  baseURL: "http://127.0.0.1:8000"
})

Axios.interceptors.response.use(
  (res) => res,
  (error) => Promise.reject((error.response && error.response.data) || 'Something went wrong')
);

Axios.interceptors.request.use(
  async (config) => {
      const token = localStorage.getItem("token");
      if (token) {
          config.headers = {
              ...config.headers,
              authorization: `Token ${token}`
          };
      }
      return config;
  },
  (error) => Promise.reject(error)
);


// ----------------------------------------------------------------------

export default Axios

export const fetcher = async args => {
  const [url, config] = Array.isArray(args) ? args : [args]
  
  const res = await Axios.get(url, { ...config })

  return res.data
}

// ----------------------------------------------------------------------

export const endpoints = {
  kanban: "/tasks",
  comments: "/comments/"
}
