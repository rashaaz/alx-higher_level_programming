#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const co = {};
    const ta = JSON.parse(body);
    for (const ii in ta) {
      const task = ta[ii];
      if (task.co === true) {
        if (co[task.userId] === undefined) {
          co[task.userId] = 1;
        } else {
          co[task.userId]++;
        }
      }
    }
    console.log(co);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
