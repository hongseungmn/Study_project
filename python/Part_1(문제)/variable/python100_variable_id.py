# 아래 코드의 결과로 출력되는 값들에 대해서 설명하시오.
# id() 함수는 무엇을 출력하는가?
# 3개의 id 출력 값중 다른 값을 출력하는 것이 있다면 몇번이고 왜 그런지 그 이유를 설명하시오.


# [1] 
a = '붕어빵'
print( a, ' --> ', id(a) )

# [2]
b = a
print( b, ' --> ', id(b) )

# [3]
a = '잉어빵'
print( a, ' --> ', id(a) )





