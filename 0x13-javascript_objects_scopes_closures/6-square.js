#!/usr/bin/node
Square1 = require('./5-square.js');
class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let myStr = '';
      for (let i = 0; i < this.height; i++) {
        myStr += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(myStr);
      }
    }
  }
}
module.exports = Square;
