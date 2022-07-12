
//전역 변수 초기화
let $view = null;
let currentIndex = 1;
let timerID = 0;
//시작부분
$(document).ready(function() {
    init(); //전역변수 초기화 및 함수 호출
    initEvent(); //이벤트 초기화 함수 등록

});
//초기화 함수
function init() {
    //view 객체를 찾아옴
    $view = $("#view");
    
}

// 이벤트 초기화
function initEvent() {
    //play 버튼 자동실행 이벤트 등록
    $("#play").click(function() {
        startAutoPlay();
    });

    //stop 버튼 멈춤 이벤트 등록
    $("#stop").click(function() {
        stopAutoPlay();
    });

    //prev 버튼 이전 이미지 출력 이벤트 등록
    $("#prev").click(function() {
        previmage();
    });

    //next 버튼 이전 이미지 출력 이벤트 등록
    $("#next").click(function() {
        nextImage();
    });
}


//자동 실행 함수
function startAutoPlay() {
    if(timerID ==0) {
        //0.01초마다 nextImage를 호출하고 있는 코드
        timerID = setInterval(function(){
            nextImage();
        },100);
    }
}

function stopAutoPlay() {
    //타이머 아이디가 존재한다면 실행되고 있다는 것이므로...
    if(timerID != 0) {
        clearInterval(timerID);
        timerID = 0;
    }
}

function previmage() {
    let index = currentIndex -1;
    //이미지의 개수가 60개이므로 첫번째 이미지이면 currentIndex가 0이 되므로
    //아래와 같이 59로 강제 설정함
    if(index <=0) {
        index = 59;
    }
    showImage(index);
}

//다음 이미지를 보여주는 함수
function nextImage(){
    //다음 이미지를 보여주기 위해서 +1을 하였다.
    let index = currentIndex +1;
    //이미지가 60개이므로 아래와 같이 설정
    if(index >= 60){
        index = 1;
    }
    showImage(index);
}
//실질적으로 이미지를 보여주는 함수
function showImage(index){
    //이미지의 속성을 설정하고 있다.
    $view.attr("src","img/"+index+".jpg");
    currentIndex = index;
    console.log("현재 이미지 번호 : " + currentIndex);
}
