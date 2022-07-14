#계산기 프로그램 만들기

from tkinter import *

window = Tk()
window.title("계산기")

display = Entry(window, width=33,bg = "yellow")
#사용자로부터 수식을 입력받고 계산 결과를 보여주는 엔트리 위젯 열 병합으로 처리
display.grid(row =0 ,column=0, columnspan=5)

#버튼에 표식될 텍스트를 리스트로 값을 설정함
button_list = [
    "7","8","9","/","C",
    "4","5","6","*"," ",
    "1","2","3","-"," ",
    "0",".","=","+"," ",
]

row_index = 1
col_index = 0

#버튼을 생성해서 리스트에 있는 값을 표식한다
# 17개의 버튼에 전부 이벤트 처리를 해야 하는데 하나의 함수를 정의해서 람다식으로 호출만
# 하게끔 아래코드에서 작성을 하였다.
#lambda t = button_text: click(t) 코드를 일반 코드로 바꾸면 아래와 같다
# def process(t=button_text)
#   click(t)


for button_text in button_list:
    Button(window,text=button_text,width=5,command=lambda t = button_text:
                                            click(t)).grid(row=row_index,column=col_index)
    col_index += 1 # 열의 인덱스를 증가함
    # 5열까지 배치가 되면 행을 바꾼다
    if col_index >4 :
        row_index +=1
        col_index = 0

window.mainloop()