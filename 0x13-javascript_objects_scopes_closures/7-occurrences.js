#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let item;
  for (item of list.flat()) {
    if (item === searchElement) {
      counter++;
    }
  }
  return counter;
};
