#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const endpoint = process.argv[2];
const fileName = process.argv[3];

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
