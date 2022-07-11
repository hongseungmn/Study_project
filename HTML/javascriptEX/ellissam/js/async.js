'use strict';

// JavaScript is synchronous;
// Execute the code block by orger after hoisting.
// hoisting : var, function declaration

// Synchronous callback

console.log('1');
setTimeout(()=> console.log('2'),1000);
console.log(3);

function printImmediately(print){
    print();
};

printImmediately(()=> console.log('hello'));


// Asynchronous callback
function printWithDelay(print,timeout){
    setTimeout(print,timeout);
};
printWithDelay(()=> console.log('async callback'),2000);