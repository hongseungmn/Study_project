#생성자에 대한 실습
# 개념 : 인스턴스를 생성하기 위해서 꼭 필요한 존재이다.
# 아울러 필드의 초기화 메서드 역할을 한다.
# __init__() 작성해줌으로써 생성자가 호출이 된다.
# 만약에 클래스에 생성자가 존재하지 않으면 인터프리터가 알아서 하나의 기본 생성자를 추가해준다.
class Person:
    name = "" #__name처럼 필드 앞에 __를 붙이면 private성질을 가지게 된다. 클래스 내부에서만 접근이 가능해진다.
    age = 0   #__가 붙지 아니하면 public 성질을 가진다. 클래스 내부와 외부 모두 접근이 가능하다.
    height = 0
    weight = 0
    address = ""
    
    #기본 생성자
    def __init__(self):
        self.name = "홍길동"
        self.age = 25
        self.height = 175
        self.weight = 79
        self.address = "경북"
        
    #getter()는 리턴값만 존재하고 매개변수는 존재하지 않는다.    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getAddress(self):
        return self.address
    print("Person의 기본 생성자 호출")
    
    #setter() 메서드
    def setName(self,name):
        self.name = name
        
    # __str()__ 멤버변수의 값을 간단하게 확인하고자 할 때 사용하면 편리하다. 자바언어의 toString()와 유사하다.
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)