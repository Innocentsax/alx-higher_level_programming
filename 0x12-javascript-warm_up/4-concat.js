#!/usr/bin/node
/*
  Write a script that prints two arguments passed to it still using the
  concept of process.argv

  Author: sammykingx

const firstArg = process.argv[2], secondArg = process.argv[3];
if (firstArg === undefined || secondArg === undefined) {
  console.log(firstArg + ' is ' + secondArg);
} else {
  console.log(firstArg + ' is ' + secondArg);
}
*/
console.log(process.argv[2] + ' is ' + process.argv[3]);
