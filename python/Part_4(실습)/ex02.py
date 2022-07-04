#섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 FtoC()

def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0))/9.0
    return temp_c

#사용자로부터 정수를 입력받아서 소수를 판별하는 함수 is_prime()을 작성
#소수면 True, 소수가 아니면 False 출력하도록 만든다.
def is_prime(num):
    temp = True
    for i in range(2,num):
        if (num%i) !=0:
            temp = True
        else:
            temp = False
            
    return temp

#함수 호출
print(is_prime(4))

#간단한 사칙연산 계산기 만들기

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return round((x / y),2)

n1 = float(input("첫 번째 수 입력"))
n2 = float(input("두 번째 수 입력"))

op = input("원하는 연산을 입력(+,-,/,*")

#연산자에 의해서 분기를 시킨다
result = 0
if op == "+":
    result = add(n1,n2)
elif op == "-":
    result = substract(n1,n2)
elif op == "/":
    result = divide(n1,n2)
elif op == "*":
    result = multiply(n1,n2)
else:
    print("잘못된 연산자입니다")
    
    
