#!/usr/bin/node
const rq = require('request');
const ur = process.argv[2];

rq.get(ur).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
