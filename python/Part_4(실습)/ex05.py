#값에 의한 호출(call by value), 값에 의한 전달(pass by value)
#함수를 호출할 때, 값이 복사가 되어진다. 호출한 곳에 영향을 끼치지 아니한다.

def change(num):
    num += 10

#파이썬에서는 모든 값들이 객체로 이루어져 있다.    
n = 100
change(n) # 값은 변하지 않는다.


#문자열 전달에 대한 실습
def change(string):
    string +="공부합니다"
    
msg = "안녕하세요"
change(msg) # 값은 변하지 않는다

#문자열에 대한 내용도 앞서 살펴본 숫자형의 객체와 동일한 변경될 수 없는 immutable object형태이다.
#파이썬의 경우는 타 언어의 call by value의 개념과는 조금은 다르다.
#그 이유는 파이썬은 모든 것을 "객체"로 판단을 하기 때문이다.
#파이썬의 이런 특성이 존재하므로 call by objective이라고도 칭한다.

