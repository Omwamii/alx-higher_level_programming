#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const starUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const res = JSON.parse(body).results;
    for (const result of res) {
      if (result.characters.includes(starUrl)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
