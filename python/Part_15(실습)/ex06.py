# 연산자 오버로딩 실습 -2
class NumBox(object):
    def __init__(self,num):
        self.num = num
        
    def __add__(self,num):
        self.num += num

    def __sub__(self,num):
        self.num -= num
        
    def __radd__(self,num):
        self.num += num
    
    def __rsub__(self,num):
        self.num -= num
        
        
        
n = NumBox(40)
# 객체와 int 간에는 연산이 이루어지지 않는다.
# 하여 클래스 안에 __add__() 특수 메소드를 재정의하면 비로소 연산이 이루어지고 출력이 되는 것을 볼 수가 있다
n + 100
print(n.num)

# __add__()를 재정의 한다고 해도 아래와 같이 자리를 바꿔버리면 에러가 발생함을 알 수가 있다
# 이때는 + 연산자는 __add__()를 호출하지 않고 __radd__()메소드를 호출한다.
110 + n
print(n.num)

n - 110
print(n.num)

110 - n
print(n.num)