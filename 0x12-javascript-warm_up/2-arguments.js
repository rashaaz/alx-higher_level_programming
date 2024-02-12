#!/usr/bin/node
const ra = process.argv.length;
console.log(ra === 2 ? 'No argument' : ra === 3 ? 'Argument found' : 'Arguments found');
