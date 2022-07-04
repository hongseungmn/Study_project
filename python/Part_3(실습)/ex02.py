#range()함수 실습

#1. range(x) 매개변수 1개짜리 함수를 이용
from re import L


sum =0 
for x in range(10):
    sum += x
print(sum)

#2. range(start,stop) 매개변수 2개짜리 함수를 이용
sum =0
for x in range(0,10):
    sum += x
    
print(sum)

#3. range(start,stop,step) 매개변수 3개짜리 함수를 이용
#range([start],stop,[step])대괄호[]로 감싸져 있는 경우 해당 값을 생략 가능하다.
sum =0;
for x in range(0,10,2):
    sum += x
print(sum)

#4. 문자열 실습
#문자열도 시퀀스의 대상에 포함된다. 하여 for문을 통해 문자를 추출하여 출력이 가능하다.
s = 'Shin Eun Hyun'
for ch in s:
    print(ch,end = " ")
    
    