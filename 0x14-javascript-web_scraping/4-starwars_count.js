#!/usr/bin/node
const rq = require('request');
const ur = process.argv[2];

rq(ur, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let output = 0;
  for (const result of JSON.parse(body).results) {
    for (const wedgeUrl of result.characters) {
      if (wedgeUrl.includes(18)) {
        output++;
      }
    }
  }
  console.log(output);
});
