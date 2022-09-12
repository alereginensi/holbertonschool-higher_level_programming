#!/usr/bin/node

// script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const id = process.argv[2];

axios.get(id)
  .then(res => {
    let count = 0;
    for (const data of res.data.results) {
      for (const num of data.characters) {
        if (num.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.log('code:', error.response.status);
  });
