#주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램 만들기
#randint()함수를 검색하여 사용법을 익힌 후 프로그램을 작성하시오

from random import *

num = randint(1,6)
#randint(a,b)함수는 a부터 b 사이에 있는 정수를 반환해주는 함수
print("주사위 눈 : ",num)

num = random()
#random()함수는 0.0부터 0.1미만의 임의의 값을 float 형태로 반환해주는 함수
print("num:",num)

num = randrange(0,101,2)
#randrange(start,end,step)함수는 start에서 stop까지 step의 값에 따라서 임의의 수를 반환해주는 함수
print("num:",num)

num = randrange(10)
#randrange(a) 함수는 0에서부터 a 미만까지의 임의의 정수값을 반환하는 함수
print("num:",num)

