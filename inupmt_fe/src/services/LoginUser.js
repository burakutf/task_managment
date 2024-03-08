import Axios from "./Axios";

export const loginUser = (username, password) => {
  const url = "login/";

  const data = {
    phone: username,
    password: password,
  };

  return Axios.post(url, data);
};
