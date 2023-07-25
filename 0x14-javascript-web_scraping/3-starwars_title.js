#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
