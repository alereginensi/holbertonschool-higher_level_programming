#!/usr/bin/node

// script that prints the title of a Star Wars movie where the episode number matches a given integer.

const axios = require('axios');
const id = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(response => {
    console.log(response.data.title);
  });
