function changeName(obj){
    obj.name = 'coder';
}

const ellie = {name: 'ellie'};
changeName(ellie);
console.log(ellie);

function showMessage(message,from = 'unknown'){
    console.log(`${message} by ${from}`);
}
showMessage('HI!');

function printAll(...args){
    for(let i =0; i< args.length; i++){
        console.log(args[i]);
    }

    for(const arg of args){
        console.log(arg);
    }

    args.forEach((arg) => console.log(arg));
}

printAll('dream','coding','ellie');


function randomQuiz(answer,printYes,printNo){
    if(answer ==='love you'){
        printYes();
    }
    else {
        printNo();
    }
};

const printYes = function() {
    console.log('yes!');
};

const printNo = function print(){
    console.log('no!');
};

randomQuiz('wrong',printYes,printNo);
randomQuiz('love you',printYes,printNo);


//Arrow Function
const simplePrint = () => console.log('simplePrint!');
const add = (a,b) => a+b;

//선언함과 동시에 호출
(function hello() {
    console.log('IIFE');
})();

