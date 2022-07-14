# 레이블에 이미지와 텍스트를 동시에 나타내기

from tkinter import *

window = Tk()
#PhotoImage 클래스는 jpg 확장자를 지원을 하지 않는다.
photo = PhotoImage(file="./imageTest.png")
#이미지는 들어가 잇는 레이블은 윈도우의 우측 배치
lbl = Label(window, image=photo)
lbl.photo = photo
lbl.pack(side=RIGHT) 
msg = "안녕하세요. 삶이 그대를 속일지라도 슬퍼하거나 노여워하지 마라."\
        "안녕하세요. 삶이 그대를 속일지라도 슬퍼하거나 노여워하지 마라."\
        "안녕하세요. 삶이 그대를 속일지라도 슬퍼하거나 노여워하지 마라."
        
# 텍스트를 출력
lbl2 = Label(window,
                justify=LEFT, #텍스트를 왼쪽정렬
                padx=10,
                text=msg).pack() 

window.mainloop()

