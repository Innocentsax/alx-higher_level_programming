#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (
  fs.existsSync(fileA) &&
fs.statSync(fileA).isFile &&
fs.existsSync(fileB) &&
fs.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);
  const stream = fs.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
