#!/usr/bin/node
const rq = require('request');
const ur = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${ur}`;

rq(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    rq(characterId, function (err, response, body) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
