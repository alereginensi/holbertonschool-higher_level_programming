#!/usr/bin/node

// prints My number: <first argument converted in integer>

if (process.argv[2] % 1 === 0) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
