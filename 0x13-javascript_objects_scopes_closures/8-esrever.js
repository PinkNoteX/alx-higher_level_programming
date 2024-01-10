#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  let len = list.length - 1;

  while (0 <= len) {
    rev.push(list[len]);
    len--;
  }
  return rev;
};
