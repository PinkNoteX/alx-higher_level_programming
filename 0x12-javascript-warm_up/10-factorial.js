#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function fact (x) {
  if ((Number.isNaN(x) || x < 2)) {
    return 1;
  } else {
    return x * fact(x-1);
  }
}

console.log(fact(arg));
