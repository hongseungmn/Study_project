# 랜덤하게 사각형을 윈도우 창에 나타내기 실습

import random
from tkinter import *

window = Tk()
canvas = Canvas(window, width=600,height=500,bg="white")
canvas.pack()

#7개의 색상을 리스트로 생성
color = ["red","orange","black","yellow","blue","violet","green"]

def draw_rect():
    x = random.randint(0,600)
    y = random.randint(0,500)
    w = random.randrange(100)
    h = random.randrange(100)
    # random.choice()는 매개변수로 들어간 시퀀스 자료형의 인덱스를 무작위로 
    # 랜덤하게 생성을 해준다.
    canvas.create_rectangle(x,y,w,h,fill=random.choice(color))

for i in range(10):
    draw_rect()

window.mainloop()