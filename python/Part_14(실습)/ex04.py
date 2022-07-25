# 내장함수와 람다식을 이용한 예제
# 1. map() 와 람다식
list_a = [1,2,3,4,5]
#f = lambda x : x * 2 #리스트의 각자의 요소에 2를 곱하여 리턴해준다
#result = map(f,list_a)
result = map(lambda x : x * 2, list_a)
print(list(result))

# 2. filter() 와 람다식
list_b = [1,2,3,4,5,6]
# filter()와 람다식을 이용하여 2의 배수를 구하고 있다.
result = filter(lambda x : x % 2 ==0,list_b)
print(list(result))