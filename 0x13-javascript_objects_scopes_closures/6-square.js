#!/usr/bin/node
const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let m = '';
      for (let j = 0; j < this.width; j++) {
        m += c;
      }
      console.log(m);
    }
  }
}

module.exports = Square;
