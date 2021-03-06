var bigPic = document.querySelector("#earth"); //큰 이미지 찾아옴
var smallPic = document.querySelectorAll(".small"); //작은 이미지 찾아옴(리스트)
var cup = document.querySelector("#earth");
var isOpen = false;

for(var i=0; i <smallPic.length;i++) {
    //작은 이미지 노드리스트들을 클릭을 하면 chagePic()가 호출이 된다
    smallPic[i].addEventListener("click",changePic);
}

function chagePic() {
    //클릭 이벤트가 발생한 대상의 src속성을 newPic에 저장
    var newPic = this.src;
    //newPic의 값을 큰 이미지의 src속성으로 대입이 되어 큰 이미지로 나타남    
    bigPic.setAttribute("src",newPic);
    //cup.src = newPic;
}

var view = document.querySelector("#view");
view.addEventListener("click",function(){
    //상세 정보가 감춰져 있다면...
    if(isOpen == false) {
        //상세 정보를 보이기
        document.querySelector("#detail").style.display = "block";
        view.innerHTML = "상세 설명 닫기"; // 내용 수정
        isOpen=true;
    }
    else {
        document.querySelector("#detail").style.display = "none";
        view.innerHTML = "상세 설명 보기"; // 내용 수정
        isOpen=false;
    }
});