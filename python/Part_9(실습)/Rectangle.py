from zmq import ctx_opt_names
from Shape import *

#자손 클래스 Rectangle 정의

class Rectangle(Shape):
    width = 0
    height = 0
    def __init__(self,cx,cy):
        Shape.__init__(self) #조상 클래스의 생성자 호출
        self.cx = cx
        self.cy = cy
        # 사각형의 높이, 폭을 임의의 수로 결정
        self.width = random.randrange(20,100)
        self.height = random.randrange(20,100)
        print("width: ",self.width, "           height: ",self.height)
        
        
        
    #조상 클래스 drawShape() 를 오버라이딩
    def drawShape(self):
        #사각형 그리기
        sx1,sy1 = 0,0 #좌측 상단의 좌표값
        sx2,sy2 = 0,0 #우측 하단의 좌표값
        
        
        sx1 = self.cx - self.width/2
        sy1 = self.cy - self.height/2
        
        sx2 = self.cx + self.width/2
        sy2 = self.cy + self.height/2
        print("sx1 : ",sx1, "       sy1 : ",sy1)
        print("sx2 : ",sx2, "       sy2 : ",sy2)
        
        #펜의 색상과 두께를 조상 클래스의 메서드를 호출
        self.setPen() 
        self.myTurtle.penup() #펜을 드는 메서드
        self.myTurtle.goto(sx1,sy1) #  펜을 좌측 상단으로 이동
        self.myTurtle.pendown() #펜을 내리는 메서드
        self.myTurtle.goto(sx1,sy2)
        self.myTurtle.goto(sx2,sy2)
        self.myTurtle.goto(sx2,sy1)
        self.myTurtle.goto(sx1,sy1)
        
        
#Shape 클래스의 실행

#왼쪽 마우스를 클릭하면 호출되는 함수
def screenLeftClick(x,y):
    rect = Rectangle(x,y)
    rect.drawShape()
    
if __name__ =="__main__":
    turtle.title("클래스를 이용한 사각형 그리기")
    #아래 코드는 터틀 그래픽 판에서 마우스 왼쪽 버튼이 클리이 되는 것을 감지하는 리스너 메서드이다.
    #1은 왼쪽 버튼, 2는 휠, 3은 우측버튼
    turtle.onscreenclick(screenLeftClick,1)
    turtle.done() #터틀 그래픽 창을 닫히지 않게끔 하는 메서드