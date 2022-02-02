#!/usr/bin/node
// JS Script
let fs = require('fs');
fs.readFile(process.argv[2], function (err, contents) {
  if (!err) {
    console.log(contents.toString().trim());
  } else {
    console.log(err);
  }
});
