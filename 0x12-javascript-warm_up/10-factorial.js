#!/usr/bin/node

// script that computes and prints a factorial
const num = parseInt(process.argv[2]);
function factorial (num) {
  if (num === 0 || Number.isNaN(num)) return (1);
  return (num * factorial(num - 1));
}
console.log(factorial(num));
