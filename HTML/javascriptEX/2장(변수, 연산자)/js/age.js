function calc() {
    var currentYear = 2022; //올해 년도의 저장을 변수 currentYear에 저장함.
    //사용자로부터 입력을 받은 값으로 변수 birthYear에 저장함
    var birthYear = prompt("태어난 년도를 입력하세요.","YYYY");
    //변수 age를 0으로 초기화
    var age = 0;
    //실제 나이를 구하기 위한 코드
    age = currentYear - birthYear;
    //document는 현재 웹브라우저의 페이지를 의미하고 querySelector()는
    //id가 result인 웹 요소(div)를 의미한다. innerHTML은 대입한 값으로 
    //HTML 문서에 대치함을 의미한다.
    document.querySelector("#result").innerHTML = 
    "당신의 나이는 " + age + "세 입니다";
}