# 유용한 모듈 사용해보기
# copy 모듈 : 객체를 복사할 때 사용하는 모듈이다
# 1. 얕은 복사(shallow copy) : 객체의 참조값(주소)만 복사되고 객체는 공유가 되버린다
# 원본 객체에 영향을 끼친다. 완벽한 복사가 아니다
# 2. 깊은 복사(deep copy) : 독립된 객체를 복사해준다. 원본객체에 영향을 미치지 않는다
# 완벽한 복사이다

import copy
colors = ["red","blue","green"]
clone = copy.deepcopy(colors)   #깊은 복사가 발생한다
clone[0] = "빨간색"
print(colors)
print(clone)

# random 모듈 사용해보기
# random 모듈 : 난수를 발생할 때 사용하는 모듈이다.
# randint() -> 정수 범위의 난수를 발생하고자 할 때 사용한다
import random
# 1 ~ 6 사이의 값을 랜덤하게 출력해준다
print("주사위의 눈 : ", random.randint(1,6))

# random() -> 0.0 ~ 1.0 미만의 난수를 발생시킨다
print("random() : ",random.random())

# randrange(start, stop, [,step]) => start 와 stop 값의 사이의 수를 랜덤하게 발생시킨다
# stop 옵션이다
print("0 ~ 100 사이의 난수 : ",random.randrange(0,101))
print("0 ~ 100사이의 3의 배수 중에 난수 : ",random.randrange(0,101,3))

# choice() -> 주어진 시퀀스의 항목을 랜덤하게 발생시킨다
list1 = ["홍성민","김연아","손연재","추신수"]
print(random.choice(list1))

# shuffle() -> 리스트의 항목을 랜덤하게 섞어주는 함수이다
list2 = [ [x] for x in range(10)]
print("섞기 전 : ",list2)
random.shuffle(list2)
print("섞은 후 : ",list2)


# sys 모듈 실습해보기
# sys 모듈은 시스템에 관련된 내용을 파이썬 인터프리터에게 다양한 정보를 제공하는 모듈
import sys
print("파이썬 설치 경로 : ",sys.prefix)
print("파이썬 버전 : ",sys.version)


# time 모듈
import time
print(time.time())      # 1970년 1월1일 자정 이후 흐른 절대시간을 초단위로 출력함
#프로그램 성능 테스트, 단위 테스트에 많이 사용된다
def fib_num(n):
    a, b = 0, 1
    while b < n:
        print(b,end=" ")
        a, b = b, a + b
    print()

start = time.time()     #시작값
fib_num(1000)
end = time.time()       #종료값
print("fib_num() 실행 시간(초) : ",end-start)
#asctime()는 현재 날짜와 시간을 문자열 형태로 표식해준다
print("현재 날짜 및 시간 : ",time.asctime())

#sleep() : 프로그램을 일시정지시키는 함수
for i in range(10,0,-1):
    print(i,end=" ")
    time.sleep(1)   #1초간 일서정지
print("완료!!!")

#calendar 모듈 사용하기
#2016.8월 달력 출력하기
import calendar
cal = calendar.month(2016,8)
print(cal)