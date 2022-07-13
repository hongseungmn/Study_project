# 배치 관리자에 대한 실습
# 1. Pack : 압축 배치 관리자
# 위젯들을 사각형 블록으로 간주하여 컨테이너 위젯 안에 상하로 배치한다.

from tkinter import *

window = Tk()

# Button(window, text="박스 #1", bg="red",fg="red").pack()
# Button(window, text="박스 #2", bg="green",fg="green").pack()
# Button(window, text="박스 #3", bg="orange",fg="orange").pack()


# 2. Gird : 격자 배치 관리자
# 루트 윈도우를 테이블의 셀로 분할되고, 각 위젯은 특정한 셀에 배치된다.
# 얼마나 많은 행과 열이 실제로 필요한지를 추적하고, 또한 가장 큰 위젯을
# 수용할 수 있도록 행과 열의 크기를 결정한다. 모든 행이 같은 높이가 될 필요는 없다.
# 동일한 폭을 가질 필요도 없다.

# b1 = Button(window, text="박스 #1", bg="red",fg="red")
# b2 = Button(window, text="박스 #2", bg="green",fg="green")
# b3 = Button(window, text="박스 #3", bg="black",fg="black")
# b4 = Button(window, text="박스 #4", bg="blue",fg="blue")

# b1.grid(row=0,column=0)
# b2.grid(row=0,column=1)
# b3.grid(row=1,column=0)
# b4.grid(row=1,column=1)

# 3. Place : 절대 배치 관리자 
# 절대 위치를 사용하여 위젯을 배치시킨다. x, y를 매개변수로 이용한다.
# x,y 매개변수는 좌표값에 해당하여 절대적인 위치에 위젯을 배치시킨다.
window.geometry("500x500")
b1 = Button(window, text="박스 #1", bg="red",fg="red")
b1.place(x = 10, y= 10)
b2 = Button(window, text="박스 #2", bg="green",fg="green")
b2.place(x = 100, y= 50)
b3 = Button(window, text="박스 #3", bg="black",fg="black")
b3.place(x = 100, y= 100)
b4 = Button(window, text="박스 #4", bg="blue",fg="blue")
b4.place(x = 200, y= 150)

window.mainloop()
