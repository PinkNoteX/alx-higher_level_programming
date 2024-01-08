#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
  for (let id = arg; id > 0; id--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
