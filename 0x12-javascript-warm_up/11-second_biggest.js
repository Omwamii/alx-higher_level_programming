#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const myNums = [];
  for (let i = 2; i < process.argv.length; i++) {
    myNums.push(parseInt(process.argv[i]));
  }
  let largest = myNums[0];
  for (let i = 0; i < myNums.length; i++) {
    if (myNums[i] > largest) { largest = myNums[i]; }
  }
  const index = myNums.indexOf(largest);
  myNums.splice(index, 1);

  largest = myNums[0];
  for (let i = 0; i < myNums.length; i++) {
    if (myNums[i] > largest) { largest = myNums[i]; }
  }
  console.log(largest);
}
