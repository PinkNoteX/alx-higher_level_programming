#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h = parseInt(h)) > 0 && (w = parseInt(w)) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
