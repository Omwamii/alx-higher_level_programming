#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body);
    const tasks = {};
    for (const task of res) {
      if (task.completed) {
        if (task.userId in tasks) {
          tasks[task.userId] += 1;
        } else {
          tasks[task.userId] = 1;
        }
      }
    }
    console.log(tasks);
  }
});
