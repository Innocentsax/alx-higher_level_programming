#!/usr/bin/node
let count = Number(process.argv[2]);
if (isNaN(count)) {
  console.log('Missing Number of occurrences');
} else if (count > 0) {
  for (count; count > 0; --count) {
    console.log('C is fun');
  }
}
