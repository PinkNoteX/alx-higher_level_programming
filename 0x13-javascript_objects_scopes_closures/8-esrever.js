#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  let len = list.length - 1;
  while (len >= 0) {
    rev.push(list[len]);
    len--;
  }
  return rev;
};
