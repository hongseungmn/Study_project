# 아래 코드의 is, == 연산자의 결과로 출력되는 값을 예상하여 말해보시오.
# 결과는 True, False 값으로 출력된다.


# [1] : 숫자
a = 101
b = 100 + 1
print( '[1-1] a is b = ', a is b ) # true
print( '[1-2] a == b = ', a == b ) # true


# [2] : 문자열
c = 'korea'
d = 'korea'
print( '[2-1] c is d = ', c is d ) # true
print( '[2-2] c == d = ', c == d ) # true


# [3] : 리스트
e = [ 1, 2, 3, 4, 5 ]
f = [ 1, 2, 3, 4, 5 ]
print( '[3-1] e is f = ', e is f ) # false
print( '[3-2] e == f = ', e == f ) # true









