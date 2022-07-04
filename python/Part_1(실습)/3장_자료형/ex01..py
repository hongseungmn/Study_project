#파이썬에서의 자료형
#int 형을 출력
print(type(17))

#float 형을 출력
print(type(10.7779))

#str 형을 출력
print(type('hello'))

from math import *
from xml.etree.ElementTree import PI

r = 5.0
volume = 4.0/3.0 * pi * r ** 3
volume = 4.0/3.0 * pi * pow(r,3)
print(volume)
print("구의 부피 : " + str(volume))
# 문자열 + float은 타입이 일치가 안되어 문자열을 생성할 수 없음
print(pi)

outer_area = 4 * pi * pow(r,2)
print("구의 겉넓이 : ",outer_area)