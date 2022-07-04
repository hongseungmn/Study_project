#함수에 대한 실습
#1.함수는 프로그램 안에서 중복된 코드를 제거한다.
#2.복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
#3.함수는 한번 만들어두면 재사용이 얼마든지 가능하다.
#4.함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.


#간단한 함수
def say_hello(name):        #함수의 선언부
    print("안녕하세요"+ name)  #함수의 구현부(정의부,몸체)
    
say_hello("홍성민")
    
#파이썬에서는 오버로딩의 개념이 없다.
#같은 함수의 이름이라면 마지막에 정의되어진 함수만 인식하게 된다. 하여, 함수명은 유니크한 값으로 설정한다.
def say_hello(name,msg):
    print("안녕하세요",name,msg)
    
say_hello("홍성민","반갑습니다")

#값을 반환하는 함수 예제
def get_sum(start,end):
    sum =0
    for i in range(start,end+1):
        sum +=i
    return sum

result = get_sum(1,10)


# 정수를 사용자로부터 입력받아서 x제곱한 값을 반환하는 함수
def sqrt_num(num,x):
    for i in range(x-1):
        num *= num
       
    return num

num = int(input("제곱하고 싶은 정수를 입력하세요 : "))
print(sqrt_num(num,2))


#두 개의 정수를 입력받아서 두 수 중에서 더 큰수를 찾아서 큰수를 리턴하는 함수

def bigger(x1,x2):
    big_num =0
    if x1>x2:
        big_num =x1
    elif x1 < x2:
        big_num = x2
    elif x1 == x2:
        big_num = -1
        
    return big_num

a = int(input("두 수를 입력하세요"))
b = int(input("두 수를 입력하세요"))
print(bigger(a,b))