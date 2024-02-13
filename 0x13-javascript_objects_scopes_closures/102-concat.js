#!/usr/bin/node
const sh = require('sh');

const ss = sh.readFileSync(process.argv[2]).toString();
const sm = sh.readFileSync(process.argv[3]).toString();
sh.writeFileSync(process.argv[4], ss + sm);
