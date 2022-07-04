#구의 부피를 계산하는 함수 sphereVolume()를 작성하여 보자

from math import pi

def sphereVolume(r):
    volume = 4/3 * pi * r**3
    return volume

print(sphereVolume(3))

#일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력
#패스워드의 길이는 6개자리로 한정한다.
#난수가 발생되는 범위 값을 지정을 아래와 같이 한다.
#난수 발생 문자열 : "0123456789"

import random

def get_Password():
    num_str = "0123456789"
    password = ""
    
    for i in range(6):
        index = random.randrange(len(num_str))
        password = password + num_str[index]
        
    return password

print("본인 인증을 위해서 발송한 숫자를 입력하세요",get_Password())


#사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는 함수를 작성
def decTobin(num):
    binary =""
    
    while num != 0:
        value = num%2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        
        num = num // 2
        
    return binary

decNum = 63
print(decTobin(decNum))
#파이썬 내장함수
bin(10)
oct(10)
hex(10)
