#추상클래스의 실습
#추상 클래스 : 클래스 안에 최소 추상메서드가 1개 이상 존재하면 그 클래스를 추상클래스라고 함
#abc(abstract base class 약자) 모듈을 이용하여 만든다
# @abstractmethod라는 어노테이션을 추상메서드 위에 붙여준다
#추상메서드는 선언부만 존재하고 구현부는 없는 메서드이다.
#추상클래스는 인스턴스를 절대로 생성할 수가 없다.
from abc import *

class StudentBase(metaclass = ABCMeta):
    #아래 어노테이션은 인터프리터에게 study메서드가 추상 메서드이다.
    @abstractclassmethod
    def study(self):
        pass
        
    @abstractclassmethod
    def go_to_school(self):
        pass

#Student클래스는 인스턴스를 만들 수 없다. 그 이유는 추상 메서드 1개를 재정의를 하지 않았기 때문
class Student(StudentBase):
    def study(self):
        print("공부를 합니다")
        
class student1(Student):
    def go_to_school(self):
        print("학교를 갑니다.")

if __name__ =="__main__":
    #추상클래스는 절대로 인스턴스를 생성할 수 없다.
    #상속을 통하여 자손클래스에서 추상 메서드를 전부 오버라이딩을 했을 때 인스턴스 생성이 중요하다.
    student = student1()
    student.go_to_school()
    #추상클래스의 용도 : 추상클래스를 상속받는 각각의 자손클래스에서
    #다른 내용으로 구현될 것을 예상하고 뼈대만 만든다라는 것이다.