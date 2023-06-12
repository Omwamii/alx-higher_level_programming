#!/usr/bin/node
if (parseInt(process.argv[2])) {
  let size = parseInt(process.argv[2]);
  const myChar = 'X';
  let result = '';
  for (let i = 0; i < size; i++) {
    result += myChar;
  }
  while (size > 0) { console.log(result); size--; }
} else {
  console.log('Missing size');
}
