#!/usr/bin/node

// script that computes the number of tasks completed by user id.

const axios = require('axios');
const arg = process.argv;

axios.get(arg[2])
  .then(response => {
    const dic = {};
    const data = response.data;
    for (const x of data) {
      if (x.completed === true) {
        if (dic[x.userId] !== undefined) {
          const status = dic[x.userId];
          dic[x.userId] = status + 1;
        } else {
          dic[x.userId] = 1;
        }
      }
    }
    console.log(dic);
  });
