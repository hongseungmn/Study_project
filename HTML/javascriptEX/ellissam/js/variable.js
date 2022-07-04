'use strict';

console.log("Hello, World!");


//전역변수와 지역변수

let globalNmae = 'global name';

{
    let name = 'ellie';
    console.log(name);
    name = 'seungmin';
    console.log(name);
    console.log(globalNmae);
}

//console.log(name); // error!!
console.log(globalNmae);

// var hoisting : 변수를 끌어올려 어디에서 사용할 수 있는 것
// var는 block scope가 없기 때문에 문제가 될 수 있다.
// 따라서 이제는 let을 통해 변수를 선언한다

// const : 포인터를 잠궈 값을 변경하지 못하게 만듬 immutable data type(변경 불가) <==> let

// variable types

const count = 17; // integer
const size = 17.1; // decimal number

console.log(`value: ${count}, type: ${typeof count}`);
console.log(`value: ${size}, type: ${typeof size}`);

//number - speicla numeric values : infinity, -infinity, Nan
const infinity = 1 / 0;
const negativeInfinity = -1 / 0;
const nAn = 'not a number' / 2
console.log(infinity);
console.log(negativeInfinity);
console.log(nAn);

//bigInt
const bigInt = 12312334346342524252132423232242n;
console.log(`value: ${bigInt}, type: ${typeof bigInt}`);

//string
const char = 'c';
const brendan = 'brendan';
const greeting = 'hello' + brendan;
console.log(`value: ${greeting},type: ${typeof greeting}`);
const helloBob = `hi ${brendan}!`;
console.log(`value: ${helloBob}, type: ${typeof helloBob}`);
console.log('value: ' + helloBob + ' type: '+ typeof helloBab);


//object

const ellie = { name: 'ellie', age: 20}


//Dynamic typing : dynamically typed language

let text = 'hello';
console.log(`value: ${text}, type: ${typeof text}`);
console.log(text.charAt(0));
text = 1;
console.log(`value: ${text}, type: ${typeof text}`);
text = '7' + 5;
console.log(`value: ${text},type: ${typeof text}`);
text = '8' / '2';
console.log(`value: ${text}, type: ${typeof text}`);


