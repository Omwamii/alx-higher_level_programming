#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const stringData = process.argv[3];

// Writing to the file asynchronously
fs.writeFile(filePath, stringData, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
