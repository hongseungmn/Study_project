# fibi 모듈을 가져오고 있다
import fibo

# fibo 모듈명.함수명 호출을 하고 있는 형태이다
fibo.fib_num(1000)
print(fibo.fib_list(100))


# 아래는 모듈에서 특정함수만 가져오고 싶을 때 사용하는 방법
from fibo import fib_num
from fibo import fib_list

fib_num(1000)
print(fib_list(100))

# * 는 fibo 모듈에 있는 모든 것(변수, 함수, 클래스)을 가져오라는 뜻이다
from fibo import *