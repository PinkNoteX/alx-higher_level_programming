#!/usr/bin/node
const rq = require('request');
const ur = process.argv[2];

rq(ur, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const done = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (done[task.userId]) {
        done[task.userId]++;
      } else {
        done[task.userId] = 1;
      }
    }
  }
  console.log(done);
});
