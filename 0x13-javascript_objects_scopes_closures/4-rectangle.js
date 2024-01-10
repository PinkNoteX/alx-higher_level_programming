#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h = parseInt(h)) > 0 && (w = parseInt(w)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  print () {
    for (let id = 0; id < this.height; id++) {
      console.log('X'.repeat(this.width));
    }
  }
};
