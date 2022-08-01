#!/usr/bin/node

// prints the addition of 2 integers

const i = process.argv[2];
const x = process.argv[3];
function add (a, b) {
  console.log(a + b);
}
add(parseInt(i), parseInt(x));
