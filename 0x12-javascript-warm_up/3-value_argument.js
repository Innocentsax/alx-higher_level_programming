#!/usr/bin/node

const value = process.argv[2];
if (value === undefined) {
  console.log('No argument');
} else {
  console.log(value);
}
