#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
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
