# 특수 메소드 : 인스턴스 간에 산술연산과 비교연산을 해주는 메소드
# ex) 인스턴스 a,b가 존재한다면 a+b 를 하게 되면 주소 + 주소가 되는
# 형태이기 때문에 연산 자체가 불가하다.
# +연산이 가능하게끔 하기 위해서 __add()__클래스 안에 메소드로
# 정의를 해주면 피연산자가 인스턴스라면 + 연산을 하게 되면 자동으로
# __add()__호출해준다.

# == 연산 실습
class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    # 2개의 인스턴스를 매개변수로 받는다.(주소값 공유)
    def __eq__(self, other):
        print("__eq__() 호출됨")
        return self.radius == other.radius


# Vector2D 클래스 정의
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 특수 메소드 __add__()정의(2개의 인스턴스를 매개변수를 받는다)
    def __add__(self, other):
        # 인스턴스의 더하기 연산을 하고 그 해당하는 값을 가지고 새로운
        # 인스턴스를 생성하여 리턴해준다.
        print("call")
        return Vector2D(self.x + other.x, self.y + other.y)

    # 특수 메소드 __sub__()정의(2개의 인스턴스를 매개변수를 받는다)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # 특수 메소드 __eq__()정의(2개의 인스턴스를 매개변수를 받는다)
    def __eq__(self, other):
        return Vector2D(self.x == other.x, self.y == other.y)

    # 인스턴스의 멤버변수들의 값을 출력해주는 메서드이며
    # print(인스턴스명) 자동으로 호출이 되는 메서드이다.
    def __str__(self):
        return "(%g,%g)" % (self.x, self.y)


# 특수 메서드를 이용하여 len() 새롭게 메소드 다른 용도로 정의를 해보는 실습
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "제목 %s, 저자 : %s, 페이지 수 : %d" % \
            (self.title, self.author, self.pages)
        # len() 함수를 페이지수를 리턴하게끔 만듬

    def len(self):
        return self.pages


if __name__ == "__main__":
    circle1 = Circle(10)
    circle2 = Circle(10)
    # 본래 주소값끼리의 연산은 불가능하다. 인스턴스간의 ==연산자는 __eq()__메소드를 호출하는 것이다.
    if circle1 == circle2:
        print("원의 반지름이 동일합니다.")

    v1 = Vector2D(5, 2)

    v2 = Vector2D(5, 3)
    v3 = Vector2D(5, 4)
    vector_result1 = v1+v2
    print(vector_result1)

    vector_result2 = v1-v2
    print(vector_result2)

    if(v1 == v2):
        print("v1과 v2는 논리적 동등한 인스턴스 입니다")

    book = Book("Python", "brother Coding", 874)
    print(book)
    print("책의 페이지 수 : ", book.len())
