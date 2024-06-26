const axios = require('axios');

const query = "explain the content in the file";
const data = { query };

axios.post('http://localhost:5000/query', data)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
