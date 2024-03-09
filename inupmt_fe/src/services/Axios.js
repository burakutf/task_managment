import axios from "axios"

const Axios = axios.create({
  baseURL: "https://api-dev-minimal-v510.vercel.app"
})

export default Axios

export const fetcher = async args => {
  const [url, config] = Array.isArray(args) ? args : [args]
  
  const res = await Axios.get(url, { ...config })

  return res.data
}

// ----------------------------------------------------------------------

export const endpoints = {
  kanban: "/api/kanban"
}
