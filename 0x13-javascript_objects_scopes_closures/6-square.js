#!/usr/bin/node

const sq = require('./5-square');
module.exports = class Square extends sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let id = 0; id < this.height; id++) {
      console.log(c.repeat(this.width));
    }
  }
};
