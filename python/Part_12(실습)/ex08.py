# Canvas 의 메서드 
#coords() : 좌표를 변경하는 메서드
#itemconfig() : 색상을 변경하는 메서드
# delete() : 선, 도형 등을 삭제하는 메서드


from tkinter import *

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.pack()

#선을 그려본다
#선에서 fill은 색상이고, width는 선의 굵기가 된다.
line1 = canvas.create_line(0,0,500,500,fill="BLUE")
line2 = canvas.create_line(0,0,500,0,fill="RED",width=5)
#line1의 좌표를 변경한다
canvas.coords(line1,250,0,250,0)

#line2에 색상을 변경한다
canvas.itemconfig(line2,fill="orange")

rect1 = canvas.create_rectangle(50,50,200,200,fill="yellow")
rect2 = canvas.create_rectangle(200,200,300,400,fill="red",outline="blue",width=10)

#rect1을 삭제해보기
canvas.delete(rect1)

#캔버스에 그려진 선, 도형을 다 삭제하기
canvas.delete(ALL)

# 사각형에 내접한 원 그리기
canvas.create_arc(10,10,100,150,extent=90,fill="red",outline="yellow",width=5)

#타원 그리기
canvas.create_oval(50,50,250,350)

window.mainloop()