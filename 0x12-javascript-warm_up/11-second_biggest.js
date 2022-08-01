#!/usr/bin/node

// searches the second biggest integer in the list of arguments.

const array = process.argv;
const newArray = [];
for (let i = 2; i < array.length; i++) {
  newArray[i - 2] = parseInt(array[i]);
}
if (array.length < 4) {
  console.log(0);
} else {
  newArray.sort();
  newArray.reverse();
  console.log(newArray[1]);
}
