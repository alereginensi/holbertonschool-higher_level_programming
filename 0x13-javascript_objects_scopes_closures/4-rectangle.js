#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) console.log('X'.repeat(this.width));
}

  double () {
    this.width *= 2;
    this.width *= 2;
  }

  rotate () {
    const rotation = this.width;
    this.width = this.height;
    this.height = rotation;
  }
}
module.exports = Rectangle;
