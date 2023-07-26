#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];

request.get(endpoint, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = {};
    body.forEach((task) => {
      if (task.completed) {
        if (task.userId in tasks) {
          tasks[task.userId] += 1;
        } else {
          tasks[task.userId] = 1;
        }
      }
    });
    console.log(tasks);
  }
});
