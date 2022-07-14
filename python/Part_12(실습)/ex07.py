# 캔버스를 생성하여 직선, 원, 사각형, 다각형 등 실습하기
# 캔버스 위젯은 파이썬에서는 그래픽 기능을 제공하는 것이다.

from tkinter import *

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.pack()

#선을 그려본다
#선에서 fill은 색상이고, width는 선의 굵기가 된다.
canvas.create_line(0,0,500,500,fill="BLUE")
canvas.create_line(0,0,500,0,fill="RED",width=5)

#사각형을 그려본다.
canvas.create_rectangle(50,50,200,200,fill="yellow")
canvas.create_rectangle(200,200,300,400,fill="red")
window.mainloop()