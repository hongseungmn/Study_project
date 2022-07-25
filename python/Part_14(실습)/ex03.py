# 람다식(무명함수, 익명함수)은 이름은 없는 함수를 만드는 방법을 말한다. 이름은 없고
# 몸체만 존재하는 함수이다. 람다식은 def 키워드를 사용하지 아니한다. 아울러 return 
# 키워드도 사용하지 아니한다

# 람다식을 이용한 간단한 더하기 기능
f = lambda x, y : x + y # 람다함수를 정의
print("정수의 합 : ", f(10,100))
print("정수의 합 : ", f(10,50))

#위의 식을 일반함수로 만든다면 아래와 같다
def get_sum(x,y):
    return x + y
print("정수의 합 : ", get_sum(10,100))
print("정수의 합 : ", get_sum(10,50))

print("-"*100)
#GUI 프로그램에서 람다식을 활용한 예제, 이벤트 처리시 람다식으로 콜백함수를 지정
from tkinter import *
window = Tk()
# 이벤트 발생시 람다식을 통한 이벤트 핸들러인 콜백함수 호출
btn1 = Button(window,text="버튼1",command=lambda : print("버튼1이 눌러짐"))
btn1.pack(side=LEFT)
btn2 = Button(window,text="버튼2",command=lambda : print("버튼2이 눌러짐"))
btn2.pack(side=LEFT)
btn3 = Button(window,text="종료",command=quit)
btn3.pack(side=LEFT)
window.mainloop()