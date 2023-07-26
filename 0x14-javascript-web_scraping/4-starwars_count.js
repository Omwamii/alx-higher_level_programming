#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const starId = '18';

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const res = JSON.parse(body).results;
    for (const result of res) {
      for (const character of result.characters) {
        if (character.includes(starId)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
