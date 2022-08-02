#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
}
module.exports = Rectangle;
