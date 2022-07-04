from Person import *

if __name__ == "__main__":
    #기본 생성자 호출
    person1 = Person()
    person1.__str__()
    
    person2 = Person()
    
    #같은 필드의 값을 가지고 있지만 서로 다른 인스턴스이다.