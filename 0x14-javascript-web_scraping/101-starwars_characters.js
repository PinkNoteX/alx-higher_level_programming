#!/usr/bin/node
const rq = require('request');
const id = process.argv[2];
const ur = `https://swapi-api.hbtn.io/api/films/${id}`;

rq(ur, async function (err, response, body) {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      rq(characterId, function (err, response, body) {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
