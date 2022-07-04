#함수가 리턴값이 없는 경우에 대한 예제
def printInfo(name,age):
    print("=================")
    print("이름 :",name)
    print("나이 :",age)
    print("=================")
    return

#디폴트 인수
#매개변수가 기본 값을 가지게 하는 방법
#hello()는 매개변수 2개를 가지지만 디폴트 인수가 있어서 함수 호출시 name에 대응되는 인수 값만 가지고도 호출이 가능하다.
def hello(name,msg="hello"):
    print("Hi",name)
    print(msg)
    
#키워드 인수
#통상 프로그래밍 언어라면 함수의 매개변수의 위치를 기준으로 해서 해당 인수를 매칭을 해줌으로써 함수에 값이 전달된다.
#이것을 다른 말로 위치 인수 방식이라고 한다.
def calc(x,y,z):
    return x + y + z

#통상적으로 calc()를 호출시에는 위치 인수방식
#키워드 인수 형태로 호출하는 방법
print(calc(y=10,z=100,x=1000))