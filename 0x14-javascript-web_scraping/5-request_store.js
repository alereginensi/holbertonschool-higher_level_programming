#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file.

const axios = require('axios');
const arg = process.argv;
const fs = require('fs');

axios.get(arg[2])
  .then(response => {
    const content = response.data;
    fs.writeFile(process.argv[3], content, error => {
      if (error) {
        console.log(error);
      }
    });
  });
