#!/usr/bin/node

/* This script will import the rectangle module for the Square class
  The constructor will take only one argument: size
*/
import Rectangle


class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = class Square {};
