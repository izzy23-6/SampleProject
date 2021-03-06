import { authHeader } from '../Auth';

const apiUrl = 'http://localhost:8000/'

export const userService = {
    login,
    logout,
    // getAll
};

 function login (username, password) {
     return new Promise((resolve, reject) => {
            const payload = {
                username: username,
                password: password
            }
            axios.post(`${apiUrl}api/user/login/`, payload)
            .then(response => {
                    console.log(response);
                    // token = response.data.token
                    //  if (response.token) {
                    //      // store user details and jwt token in local storage to keep user logged in between page refreshes
                         localStorage.setItem('user', response.data.token);
                    //     }
                        
                        resolve(response)
                        // return resp;
        })
    })
}



function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

function getAll() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return axios(`${apiUrl}/users/logout/all`, payload).then(handleResponse);
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text)
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    })
}
