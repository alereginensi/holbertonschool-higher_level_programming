#!/usr/bin/node

// prints a square
const x = process.argv[2];
if (x % 1 !== 0) {
  console.log('Missing size');
} else {
  for (let n = 0; n < x; n++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
