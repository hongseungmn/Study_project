// Object 
'use strict';

//1. Literals and properties. 
const obj1 = {};
const obj2 = new Object();

function print(person){
    console.log(person.name);
    console.log(person.age);
}

const ellie = {name : 'ellie',age : 4};
print(ellie);

ellie.hasJob = true;
console.log(ellie.hasJob);
// can delete properties later


// Computed properties
// key sould be always string
console.log(ellie.name);
console.log(ellie['name']);
ellie['hasJob'] = true;
console.log(ellie.hasJob);

function printValue(obj,key){
    console.log(obj.key);
}

printValue(ellie,'name');
printValue(ellie,'age');


// 3. Property value shorthand

const person1 = {name: 'bob', age: 2};
const person2 = {name: 'steve', age: 3};
const person3 = {name: 'bob', age: 4};
const person4 = {name: 'bob', age: 30};
console.log(person4);

// Constructor  Function

function Person(name, age){
    this.name = name;
    this.age = age;
}

// 5. in operator
console.log('name' in ellie);
console.log('age' in ellie);


// 6. for..in vs for..of

console.clear();
for(key in ellie){
    console.log(key);
}

const array = [1,2,3,4,5];

for(value of array){
    console.log(value);
}

for(let i =0; i < array.length; i++){
    console.log(array[i]);
}


// 7. cloning

const user = {name : 'ellie',age:'20'};
const user2 = user;

// old way
const user3 = {};
for(key in user){
    user3[key] = user[key];
}

console.clear();
console.log(user3);


// another exanple
const fruit1 = {color: 'red'};
const fruit2 = {color: 'blue', size: 'big'};
const mixed = Object.assign({}, fruit1, fruit2);
console.log(mixed.color);
console.log(mixed.size);ㅇ