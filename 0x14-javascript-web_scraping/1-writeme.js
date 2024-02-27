#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];
const fd = process.argv[3];

fs.writeFile(fp, fd, 'utf-8', function (err) {
  if (err) { console.log(err); }
});
