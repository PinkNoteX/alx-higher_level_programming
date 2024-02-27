#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];

fs.readFile(fp, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
