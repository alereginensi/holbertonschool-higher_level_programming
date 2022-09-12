#!/usr/bin/node

// script that prints all characters of a Star Wars movie

const axios = require('axios');
const movie = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${movie}`)
  .then(response => {
    for (const character in response.data.characters) {
      axios.get(response.data.characters[character])
        .then(response => {
          console.log(response.data.name);
        });
    }
  });
