#클래스 2개를 만드는데 먼저 Figure 클래스를 만들고 생성자에서 Width와 Height를 받아서 초기화한다
#그다음 Quadrangle 클래스를 만들어 출력

class Figure(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
class Quadrangle(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    #연산자 + 중복 정의
    def __add__(self,other):
        return Quadrangle(self.width + other.width,self.height+ other.height)
    

quad = Quadrangle(2,3)
figure = Figure(3,4)
print("너비의 합 : ",quad.width + figure.width)
print("높이의 합 : ",quad.height + figure.height)

sumQuad = quad + figure

print("합한 도형(너비,높이) :",sumQuad.width,",",sumQuad.height )

    