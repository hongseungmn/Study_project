var mRect = document.querySelector("#rect");

//mouseover 이벤트를 처리하는 부분
mRect.addEventListener("mouseover",function() {
    mRect.style.background="red"; //mRect의 배경색
    mRect.style.borderRadius="50%" //mRect 요소의 테두리 둥글게 처리
});

mRect.addEventListener("mouseout",function() {
    mRect.style.background=""; //mRect의 배경색
    mRect.style.borderRadius="" //mRect 요소의 테두리 둥글게 처리
});