'use strict';

// Array

//1. Declaration
const arr1 = new Array();
const arr2= [1,2];

//2. Index position
const fruits = ['apple','orange'];
console.log(fruits);
console.log(fruits.length);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[-1]);


console.log()

for(let i=0; i<fruits.length; i++){
    console.log(fruits[i]);
}
for(let fruit of fruits){
    console.log(fruit);
}

fruits.forEach((fruit) => console.log(fruit));

//4. Addtion,deletion,copy

//push : add and item to the end
fruits.push('straw','peach');
console.log(fruits);

//pop : remoce an item from the end
fruits.pop();
console.log(fruits);

// shift: remove an item from the benigging
fruits.shift();
fruits.shift();
console.log(fruits);

// note !! shift, unshift are slower than pop, push
// splice: remoce an item by index position
fruits.push('straw','orange','banana');
console.log(fruits);
fruits.splice(1,1);
console.log(fruits);
fruits.splice(1,1,'apple','watermelon');
console.log(fruits);

//conbine two arrays
const fruits2 = ['mango','kokonut'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);

// 5. Searching
// find the index
console.clear();
console.log(fruits);
console.log(fruits.indexOf('apple'));
console.log(fruits.indexOf('watermelon'));
console.log(fruits.indexOf('kokonut'));

// includes
console.log(fruits.includes('watermelon'));

//lastIndexOf
console.log(fruits.lastIndexOf('apple'));


// 1. Join : make a string out of an array
// 

{
    const fruits = ['apple','banana','orange'];
    const result = fruits.join(',');
    console.log(result);
}

// 2. Split make an array out of a string
{
    const fruits = ['apple','banana','orange'];
    const result = fruits.splice(',');
    console.log(result);
}

// 3. make this array look like this: [5,4,3,2,1]
{
    const array = [1,2,3,4,5];
    const result = array.reverse();
    console.log(result);
}

// 4. make new array without the first two elements
{
    const array = [1,2,3,4,5];
    const result = array.slice(2,-1);
    console.log(result);
}

class Student {
    constructor(name,age,enrolled,score){
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}

const students = [
    new Student('A',29,true,45),
    new Student('B',30,false,80),
    new Student('C',30,true,90),
    new Student('D',40,false,66),
    new Student('E',18,true,88)
];

// Find()
// 5. find a student with the score 90 
{
    const result = students.find((student)=>student.score == 90);
    console.log("-------------------------------------------");
    console.log(result);
}

// Filter()
// 6. make an array of enrolled students
{
    const result = students.filter((student)=>student.enrolled);
    console.log(result);
}

// Map()
// 7. make an array containing only the student's score
{
    const result= students.map((student) => student.score);
    console.log(result)
}

// Some, Every
// 8. check if there is a student with the score lower than 50
{
    const result = students.some((student) => student.score < 50);
    console.log(result);
    const result2 = !students.every((student) => student.score >= 50);
    console.log(result2);
}

// Reduce()
// 9. compute student's average score 
{
    const result = students.reduce((prev,curr) =>{
        console.log("----------------");
        console.log(prev);
        console.log(curr);
        return prev + curr.score ;
    }, 0);
}

// 10. make a string containing all the scores
{
    const result = students
    .map((student) => student.score)
    .filter((score) => score >= 50)
    .join();
    console.log(result);
}