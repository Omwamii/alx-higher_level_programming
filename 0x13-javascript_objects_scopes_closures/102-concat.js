#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const data1 = fs.readFileSync(file1, 'utf-8');
const data2 = fs.readFileSync(file2, 'utf-8');
const concated = (data1 + data2);
fs.writeFileSync(file3, concated);
