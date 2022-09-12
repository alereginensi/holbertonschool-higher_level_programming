#!/usr/bin/node

// script that display the status code of a GET request.
// https://nodejs.dev/en/learn/making-http-requests-with-nodejs/

const axios = require('axios');

axios
  .get(process.argv[2])
  .then(res => {
    console.log(`code: ${res.status}`);
  })
  .catch(() => {
    console.error('code: 404');
  });
