#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const da = JSON.parse(body);
  const ds = da.characters;
  for (const ii of ds) {
    req.get(ii, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dat = JSON.parse(body1);
      console.log(dat.name);
    });
  }
});
