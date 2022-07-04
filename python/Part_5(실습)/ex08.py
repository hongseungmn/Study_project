#리스트 함축
#리스트 함축은 수학에서 집합을 정의하는 것과 매우 유사하다.

#일반적 코드(리스트 함축을 사용하지 않은 경우)
squares = []
for x in range(1,11):
    squares.append(x**2)
print(squares)

#리스트 함축 개념을 이용하여 위와 똑같은 결과 출력하기
#출력식 반복문 리스트 함축 문법 : 출력식 반복문 조건문(옵션)
li_squares = [x**2 for x in range(1,11)]

#조건이 붙는 리스트 함축(조건문 if)
#조건식에 참이 되는 것만 리스트 요소로 생성시킨다.
odd_list = [x for x in range(1,21) if x%2 == 1]

gugu_list = [i*j   for i in range(2,10) 
                    for j in range(1,10)]

#문자열에 대한 리스트 함축
list1 = ["KOR","대한민국","서울특별시","한라산","END"]
first_word = [word[0] for word in list1]

#상호곱(Cross Product)
colors = ["white","brown","black"]
cars = ["granger","sonata","k4","spark"]
colors_cars = [x+"-"+y     for x in colors
                           for y in cars]



