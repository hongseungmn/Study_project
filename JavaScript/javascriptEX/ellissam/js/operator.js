'use strict'

// 1. String coacatenation

console.log('my' + 'cat');
console.log('1' + 2);
console.log(`string lierals: 1 + 2 = ${1 + 2}`);

// 2. Numeric operators
console.log(1 + 1); //add
console.log(1 - 1); //substract
console.log(1 / 1); //divide
console.log(1 * 1); //multiply
console.log(5 % 2); //remainder
console.log(2 ** 3); //exponentiation

// 3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;

const postIncrement = counter ++;

// Logical operators: ||(or), &&(and), !(not)
const value1 = false;
const value2 = 4 < 2;

// ||(or), finds the first truthy value
console.log(`or: ${value1 || value2 || check()}`); 

// 만약 or 연산자의 경우 true가 나오는 순간 뒤의 값은 계산하지 않는다.
// 따라서 함수같은 것을 뒤에 나둬야 한다.

function check() {
    for (let i = 0; i< 10; i++){
        //wasting time
        console.log('*^^*');

    }
    return true;
}

//equality 
console.log(0 == false); //true
console.log(0 === false); //false
console.log('' == false); // true
console.log('' === false); //false
console.log(null == undefined); //true
console.log(null === undefined); //false

