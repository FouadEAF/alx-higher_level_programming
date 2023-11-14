#!/usr/bin/node
const dict = require('./101-data').dict;
const new_dict = {};

Object.keys(dict).map(function (key, index) {
  if (new_dict[dict[key]] === undefined) {
    new_dict[dict[key]] = [];
  }
  new_dict[dict[key]].push(key);
});

console.log(new_dict);
