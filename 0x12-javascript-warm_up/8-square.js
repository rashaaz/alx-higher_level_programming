#!/usr/bin/node
const si = Math.floor(Number(process.argv[2]));
if (isNaN(si)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < si; i++) {
    let s = '';
    for (let j = 0; j < si; j++) s += 'X';
    console.log(s);
  }
}
