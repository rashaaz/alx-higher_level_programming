#!/usr/bin/node
const m = Math.floor(Number(process.argv[2]));
if (isNaN(m)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < m; i++) {
    console.log('C is fun');
  }
}
