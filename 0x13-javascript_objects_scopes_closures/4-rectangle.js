#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {

    } else {
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

  rotate () {
    const x = this.width;
    const y = this.height;
    this.width = y;
    this.height = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
