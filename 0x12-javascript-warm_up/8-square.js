#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
  for (let id1 = arg; id1 > 0; id1--) {
    console.log('X'.repeat(arg));
  }
} else {
  console.log('Missing size');
}
