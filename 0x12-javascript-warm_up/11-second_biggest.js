#!/usr/bin/node

const all = process.argv;

if (all.length < 4) {
  console.log(0);
} else {
  const vars = all.slice(2).sort((a, b) => b - a);
  console.log(vars[1]);
}
