'use strict';

// JSON 
// JavaScript Object Notation

// 1. Object to JSON
//stringfy(obj)
let json = JSON.stringify(true);
console.log(json);


json = JSON.stringify(['apple','banana']);
console.log(json);

const rabbit = {
    named : 'tori',
    color : 'white',
    size : null,
    birthDate : new Date(),
    jump : () => {
        console.log(`${named} can jump!`);
    },
};

json = JSON.stringify(rabbit,['name']);
console.log(json);


json = JSON.stringify(rabbit,(key,value) => {
    console.log(`key: ${key}, value: ${value}`);
    return key === 'name' ? 'ellie' : value;
});

console.log(json);

// 2. JSON to Object
//parse(json)

json = JSON.stringify(rabbit);
const obj = JSON.parse(json);
console.log(obj);
rabbit.jump();
//obj.jump();

console.log(rabbit.birthDate.getDate());
//console.log(obj.birthDate.getDate());