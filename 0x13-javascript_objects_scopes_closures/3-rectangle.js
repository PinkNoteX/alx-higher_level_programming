#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h = parseInt(h)) > 0 && (w = parseInt(w)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let id = 0; id < this.height; id++) {
      console.log('X'.repeat(this.width));
    }
  }
};
