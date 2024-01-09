#!/usr/bin/node

exports.callMeMoby = function (x, func) {
  for (let id = 0; id < x; id++) {
    func();
  }
};
