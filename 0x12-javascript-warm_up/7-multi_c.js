#!/usr/bin/node
if (parseInt(process.argv[2])) {
  let i = parseInt(process.argv[2]);
  while (i > 0) { console.log('C is fun'); i--; }
} else {
  console.log('Missing number of occurrences');
}
