#원을 나타내는 클래스를 만들고 radius를 생성자의 매개변수로 받아
#초기화하고 getter(), setter(), area() 즉, 원의 면적을 구하는 메소드를 작성하고,
#Circle 클래스에 +, > , < 연산자를 중복 정의 해보시오

import math
class Circle(object):
    def __init__(self,radius):
        self.radius = radius
        
    
    #getter() 메소드
    def getRadius(self):
        return self.radius
    
    #setter() 메소드
    def setRadius(self, radius):
        self.radius = radius
        
    #면적을 구하는 메소드
    def area(self):
        return math.pi * self.radius ** 2
    
    #산술연산자 중복정의(+)
    def __add__(self,other):
        return Circle(self.radius + other.radius)
    
    #비교연산자 중복정의(>)
    def __gt__(self,other):
        return self.radius > other.radius
    
    #비교연산자 중복정의(<)
    def __lt__(self,other):
        return self.radius < other.radius
    
    #문자열 출력
    def __str__(self):
        return "원의 반지름 : " + str(self.radius)
    
if __name__ == "__main__":
    c1 = Circle(5)
    print("c1의 반지름 : ", c1.getRadius())
    
    c2 = Circle(4)
    print("c2의 반지름 : ", c2.getRadius())
    
    c3 = c1 + c2
    print("c1의 반지름과 c2의 반지름을 합한 값 : ",c3.getRadius())
    print("c3 > c2의 결과 : ",c3 > c2)
    print("c1 < c2의 결과 : ",c1 < c2)
    
    print(c3)
    