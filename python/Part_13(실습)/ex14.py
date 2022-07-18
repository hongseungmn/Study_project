# 예외처리 실습
#예외처리의 목적은 프로그램의 정상적인 종료로 만들어 주는 것이다.
(x,y) = (2,0)
try:
    z = x / y
    print("예외가 발생하지 않았습니다")
except ZeroDivisionError:
    print("모든 수는 0으로 나눌수가 없습니다")