#!/usr/bin/node
let m = 0;

exports.logMe = function (item) {
  console.log(m + ': ' + item);
  m++;
};
