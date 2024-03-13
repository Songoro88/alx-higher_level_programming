#!/usr/bin/node
// The first argument passed is printed

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
