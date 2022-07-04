#지역변수와 전역변수의 실습

def test():
    #print(text) # 에러 발생: 함수 안에서 하나의 변수가 전역변수가 되었다가 다시 지역변수가 될 수가 없기 때문이다.
    #따라서 global text를 사용해 test()함수 안에서 전역변수인 text를 사용하겠다라는 것을 인터프리터한테 알린다.
    text = "파이썬 공부" # 전역변수의 값을 변경하고 있다.
    print(text)
    
text = "자바 공부"
print(text) # 전역변수의 값이 변경되기 전에 출력
test()
print(text) 

def test(n1,n2): #함수의 매개변수도 지역변수의 일종이다
    global a     #함수 내에서 전역변수의 a를 사용하겠다고 명시함   함
    a = 20
    n1 = n2
    n2 = n1
    b =10        #지역변수 b에 10을 할당함
    print(a,b,n1,n2)
   
a = 10
b = 20
n1 = 77
n2 = 88
test(n1,n2)
print(a,b,n1,n2)
    