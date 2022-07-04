#모듈을 활용하는 첫 번째 방법

import fibo

# #import 한 fibo모듈의 fib()를 사용하겠다라는 것이다.
# fibo.fib(1000)

# print(fibo.sum(10))


# #모듈을 활용하는 두 번째 방법
# from fibo import fib,sum
# fib(100)
# print(sum(10))


#__name__은 내장 전역변수로 인터프리터가 만들어 놓은 것이다.

#print(fibo.__name__)

#실행파일에서는 __name__이라는 내장전역변수는 __main__값을 지니게 된다.
print(__name__)



if __name__ == "__main__": # 프로그램의 시작점이 되는 형태(타 언어에서의 main함수 역할 수행)
    fibo.fib(1000)
    print(fibo.sum(10))
    
    
