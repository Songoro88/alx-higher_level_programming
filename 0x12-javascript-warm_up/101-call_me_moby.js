#!/usr/bin/node
// Executes x multiply by a function.

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
