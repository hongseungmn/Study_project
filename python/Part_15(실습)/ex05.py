# 연산자 오버로딩의 실습
# 연산자 오버로딩 : 객체에서 필요한 연산자를 재정의를 하는 것
# 연산자 중복을 위해 미리 정의된 특별한 메소드 존재 : __로 시작 __로 끝나는 특수 메소드들
# 해당 메소드를 클래스에 재정의해서 구현하며느 객체단에서 여러가지 파이썬 내장함수나
# 연산자를 재정의하여 사용이 가능하다
# 단, 사용자 정의 클래스에 한한다.

# 문자열(str 클래스)에 대한 실습
str1 = "안녕하세요"
str2 = "반갑습니다."

# str 클래스 내에 __add__() 특수메소드는 미리 정의가 되어 있기 때문에 아래와 같이 사용할 수가 있다
str3 = str1.__add__(str2)
print(str3)
print("----"*30)

class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        print("__add__()")
        # Point 객체끼리 + 연산을 정의하고 해당 인스턴스를 리턴하고 있다.
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    #Point 객체를 문자열로 표현하여 반환하는 __str__() 특수 메소드도 재정의를 해야 주소값이 출력이 되질 않는다
    def __str__(self):
        print("__str__()")
        return "Point(" + str(self.x) + ", " + str(self.y) +")"

p1 = Point(1,2)
p2 = Point(3,4)
# 객체의 주소값으로 연산이 이루어질 수 없기 때문에 TypeError가 발생함
print(p1 + p2) 
