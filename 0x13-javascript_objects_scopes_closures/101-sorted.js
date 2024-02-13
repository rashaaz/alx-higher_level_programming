#!/usr/bin/node
const dict = require('./101-data').dict;

const to = Object.entries(dict);
const v = Object.values(dict);
const val = [...new Set(v)];
const n = {};
for (const j in val) {
  const li = [];
  for (const kk in to) {
    if (to[kk][1] === val[j]) {
      li.unshift(to[kk][0]);
    }
  }
  n[val[j]] = li;
}
console.log(n);
