# python100_variable_var_constant
# 파이썬 프로그래밍 언어에서 상수란 무엇인지 설명해보시오.


# [1] : 상수란 무엇인가?
# 항상 변하지 않는 수 --> 상수
# 코드를 작성하는 과정에서 오직 하나의 데이터 값을 많이 사용하는데 이런 데이터 값을 담는 바구니 --> 상수
# 요리에 비유하면 오직 한가지 양념(설탕 or 소금)을 담는 양념통 --> 상수
# 상수에는 최초의 저장된 값만이 담겨질 수 있다. ---> 그래서 상수이다.

# 정리하면, 프로그램의 실행 도중에 데이터 값이 바뀌지 않고 항상 고정된 값 그대로 유지되는 것이 상수이다.
# 즉, 사용자가 임의로 바꾸거나 변경할 수 없는 사전에 미리 정의된 값을 가지는 것 --> 상수
# 숫자 상수, 문자 상수 등이 있다.












# python100_variable_var_constant_01
# 파이썬으로 파이 값과 중력가속도 값을 상수로 정의하시오.
# PI --> 3.14
# GRAVITY --> 9.8


# [1] : 상수 선언 및 값 할당
# 파이썬에서는 다른 언어에서 const 키워드로 상수를 지정하는 문법이 없다.
# 따라서 변수처럼 상수 변수를 선언하고 사용은 할 수 있겠지만, 강제로 값을 변경하고자 한다면 변경이 가능하다. --> 변수
# 완전한 상수(항상 바뀌지 않는 값)로 유지하고자 한다면 불가능한 것은 아니다. 별도의 추가적인 코드를 작성해서 처리해주면 가능은 하다.
PI = 3.14
GRAVITY = 9.8


# [2] : 변수를 상수처럼 사용
# 위의 PI, GRAVITY 변수를 대문자로 선언하고 값을 할당함으로써 상수 처럼 사용하겠다고 정의한다.
print( PI )
PI = 4.14  #--- 어? 변경이 되네..??? --> 변수 --;;

print( PI )





