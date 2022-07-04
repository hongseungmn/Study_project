#문제 : 원의 넓이와 둘레를 동시에 반환하는 함수를 작성하고 테스트하라
#반지름은 사용자로부터 입력을 받는다.

import math

def Circle(r):
    area = math.pi * math.pow(r,2)
    round = math.pi * (r*2)
    
    circle = (area,round)
    
    return circle

if __name__ == "__main__":
    radius = int(input("원의 반지름을 입력하시오 : "))
    circle = Circle(radius)
    print("원의 넓이는 ", circle[0],"이고 원의 둘레는 ",circle[1],"이다")
    