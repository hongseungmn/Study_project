#부분 집합 연산

SET1 = {10,20,30}
SET2 = {10,20,30}

#2개의 세트가 같은지 검사하는 법(==,!=)
print(SET1==SET2)

#부등호 연산을 이용하여 부분집합인지 아닌지를 알 수 있다.
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}

#연산자를 이용한 방법
print(SET1 > SET2)
#issubset()을 이용한 방법
print(SET2.issubset(SET1))

#상위 집합인지 확인하는 방법
#issuperset()를 이용하는 방법
print(SET1 < SET2)
print(SET1.issuperset(SET2))

#데이터 값이 집합에 포함되어 있는지 확인하는 방법
SET_STRING = set("안녕하세요.")
print(SET_STRING)

if "안" in SET_STRING:
    print("'안' 문자는 SET_STRING 세트에 포함되어 있습니다")
    
print("-----------------------------------------")
#집합연산을 할 수 있는 것이 세트라는 자료구조의 장점이다.
#합집합 : 연산자 |(파이프), union() 메서드를 사용
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}

print(SET1 | SET2)
print(SET1.union(SET2))
print(SET2.union(SET1))

#교집합은 두 개의 집합에서 겹치는 요소를 구하는 연산이다.
#방법 : 연산은 & 를 이용하거나 intersection() 이용한다.

print(SET1 & SET2)
print(SET1.intersection(SET2))
print(SET2.intersection(SET1))

#차집합은 하나의 집합에서 다른 집합의 요소를 빼고 남은 집합
#방법 : 연산자 - 를 사용하거나 difference()를 사용

print(SET1-SET2)
print(SET1.difference(SET2))
print(SET2.difference(SET1))

#all() 집합에서 모든 값이 참이어야지만 참을 리턴해준다.
# any() 집합에서 값이 하나라도 참이면 참을 리턴해준다.
SET1 = {0,20,30,40,50,60}
SET2 = {0,0,0,0,0,50}
SET3 = {0,0,0,0,0,-1}
print(all(SET1))
print(all(SET2))
print(all(SET3))

#집합이 처음부터 아예 다른지를 확인하고 싶을 때(같은 요소가 없다)
print(SET1.isdisjoint(SET2))

#pop()으로 집합의 요소를 제거할 수 있는데, 임의로 아무요소나 삭제한다.
#단, 정수의 경우는 한번 가져올 때의 패턴을 재실행해도 똑같지만,
#문자열 타입은 삭제 및 출력 패턴이 실행할 때마다 달라진다는 것을 알 수가 있다.
for _ in range(len(SET1)):
    print(SET1.pop(),end=" ")