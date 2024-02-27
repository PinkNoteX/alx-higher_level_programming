#!/usr/bin/node
const rq = require('request');
const fs = require('fs');
const ur = process.argv[2];
const fp = process.argv[3];
const fst = fs.createWriteStream(fp);

rq(ur).pipe(fst);
