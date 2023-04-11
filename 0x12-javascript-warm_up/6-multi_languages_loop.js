#!/usr/bin/node

/* This script will print multi-lines of string using loops
  Use an array of string to store strings
  Use only one console.log
  Not allowed to use if/else. Only a loop (while, for, etc)
*/

const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];

array.forEach(function (item) {
  console.log(item);
});
