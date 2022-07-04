#namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔 저장하는 자료구조이다.

#일반적인 튜플의 경우
person1 = ("홍성민",23,"man")
person2 = ("김수진",22,"waman")
for n in [person1,person2]:
    # %n이 들어가면서 튜플의 값들을 각각에 형식 지정자에 맞게끔 적용시킨다.
    print("%s는 %d세의 %s입니다." %n)
print("%s는 %d세의 %s입니다." % (person1[0],person1[1],person1[2]))


print("="*50)
#namedtuple인 경우
from collections import namedtuple
#Person 이라는 namedtuple을 정의하는 것
Person = namedtuple(typename="Person",field_names=("name age gender"))
P1 = Person(name= "김연아",age=32,gender="여")
P2 = Person(name= "손연재",age=22,gender="여")
print(id(P1))
print(P1)

for _ in [P1,P2]:
    print("%s는 %d세의 %s성 입니다." %n)
    
#일반적인 튜플은 .(접근 연산자)를 사용하지 못하고 인덱스로만 접근이 된다.
#일반적인 튜플은 값의 수정이나 변경이 이루어지지 않는 immutable object이다.
#Person(객체)이라고 정의를 해놓았고 그의 필드들이 3개가 존재하고 있기 때문에
#namedtuple은 .(접근연산자)를 이용할 수도 있지만 인덱스로도 접근이 가능하다.
print(P1.age,P1.gender,P2[0])


print("="*50)
#namedtuple의 _make() 메소드 : 기존에 생성된 namedtuple에 새로운 인스턴스를 생성해주는 메소드이다.
#_make() 안의 매개변수로 들어가는 것은 시퀀스 자료형이어야 한다.(리스트, 튜플 등)
P3 = Person._make(["홍성민",23,"남"]) 
print(P3)
#P1[0] = "김"
P1 = P1._replace(name="강백호")
P2 = P2._replace(age=100)
for i in [P1,P2,P3]:
    print("%s는 %d세의 %s성 입니다." %(i[0],i[1],i[2]))
    
    
print("="*50)
#생성되어진 Person 이라는 namedtuple의 _fields 로써 Person에 있는 필드명 tuple() 형식으로 리턴을 해준다.
print(P1._fields)

#getattr() 는 필드명으로 그 값을 출력할 때 사용한다.
print(getattr(P1,"name"))
print(getattr(P2,"name"))
print(getattr(P3,"name"))

# **(double-star-operator)는 namedtuple() 딕셔너리 자료구조를 namedtuple() 변환하여 반환한다.
dic = {"name":"신은비", "age":15,"gender":"여"}
print(dic)
print(type(dic))

P4 = Person(**dic)
print("%s는 %d세의 %s성입니다." %(P4.name, P4.age, P4.gender))