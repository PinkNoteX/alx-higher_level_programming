#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let id = 0; id < list.length; id++) {
    if (searchElement === list[id]) {
      x++;
    }
  }
  return x;
};
