#call by reference 
#함수가 호출할 때, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태가 된다.
#파이썬에서는 함수의 매개변수값이 전부 객체인데, list,dictionary 와 같은 
#mutable object 즉, 변경 가능한 객체이므로 call by objective-reference라고 한다.

def change(li):
    print("change()함수 내의 연산전의 li의 값 :",li)
    print("change()함수 내의 연산전의 li의 주소값 :",id(li))
    li += [100,200]
    print("change()함수 내의 연산전의 li의 값 :",li)
    print("change()함수 내의 연산전의 li의 주소값 :",id(li)) 
    
list = ['안녕',1,3,1,1.1]
print("호출 전의 list의 값 :",list)
print("호출 전의 list의 주소값 :",id(list))
change(list)
print("호출 후의 list의 값 :",list)
print("호출 후의 list의 주소값 :",id(list))


#mutable object 중 dictionary라는 타입이 있다.
#딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져 있다.
#딕셔너리의 키의 값은 유니크한 값이 되어야 한다. 하지만 값은 변경이 가능하다.
dic = {'name':"hongseungmin","age":14,"height":185}
#키를 주고 값을 얻어온다.
print(dic['name'])

def change(dic):
    print("change()함수 내의 연산전의 dic의 값 :",dic)
    print("change()함수 내의 연산전의 dic의 주소값 :",id(dic))
    dic['몸무게'] = 42
    print("change()함수 내의 연산전의 dic의 값 :",dic)
    print("change()함수 내의 연산전의 dic의 주소값 :",id(dic))    
    
print("호출 전의 dic 값 :",dic)
print("호출 전의 dic 주소값 :",id(dic))
change(dic)
print("호출 후의 dic 값 :",dic)
print("호출 후의 dic 주소값 :",id(dic))



