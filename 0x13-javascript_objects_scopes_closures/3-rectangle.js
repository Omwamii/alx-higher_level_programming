#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && (w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myW = '';
    for (let j = 0; j < this.width; j++) {
      myW += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(myW);
    }
  }
}

module.exports = Rectangle;
