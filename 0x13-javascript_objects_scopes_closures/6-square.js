#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let n = 0; n < this.height; n++) console.log('X'.repeat(this.width));
    } else {
      for (let n = 0; n < this.height; n++) console.log('C'.repeat(this.width));
    }
  }
}
module.exports = Square;
