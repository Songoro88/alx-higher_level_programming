#!/usr/bin/node
// Executes x multiply by a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
