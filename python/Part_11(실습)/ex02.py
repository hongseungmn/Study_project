from tkinter import * 
# 배치관리자(Layout Manager ) : 위젯들을 윈도우에 배치하는 방법; 기본값은 수직으로
window = Tk()
window.title("배치관리자") # 윈도우의 타이틀 설정
#버튼만 생성
button1 = Button(window, fg="yellow",text="버튼1",width=80,height=10)
button2 = Button(window, fg="yellow",text="버튼1",width=80,height=10)
button3 = Button(window, fg="yellow",text="버튼1",width=80,height=10)
# 루트 윈도우에 배치가 되어진다
# button1.pack()
# button2.pack()
#side의 기본값은 top으로 설정되어 수직정렬이 기본값이다
button1.pack(side=LEFT, padx=20, pady=20)
button2.pack(side=LEFT, padx=20, pady=20)
button3.pack(side=LEFT, padx=20, pady=20)

window.mainloop()