#!/usr/bin/node

// script that display the status code of a GET request.
// https://nodejs.dev/en/learn/making-http-requests-with-nodejs/

const axios = require('axios');

axios.get(process.argv[2])
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    console.log(`code: ${error.response.status}`);
  });
