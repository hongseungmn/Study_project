'use strict';

{
    const calculate = function(oper,num1,num2){
        if (oper === '+'){
            return num1 + num2;
        }
        else if (oper === '-'){
            return  (num1 > num2) ? num1 - num2 : num2 - num1;
        }
        else if (oper === '/'){
            return num1 / num2;
        }
        else if (oper === '*'){
            return num1 * num2
        }
    };

    const result = calculate('+',3,4);
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
    new Student('B',28,false,80),
    new Student('C',30,true,90),
    new Student('D',40,false,66),
    new Student('E',18,true,88),
];

{
    const result = students.some((student) => student.score < 50);
    console.log(result);
    const result2 = !students.every((student) => student.score >= 50);
    console.log(result2);
}

{
    const li = [1,2,3];
    li.push(20);
    console.log(li);
    
}