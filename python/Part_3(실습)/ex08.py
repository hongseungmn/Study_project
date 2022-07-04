#중첩루프에 대한 실습
#중첩 루프는 반복문 안에 또다른 반복문이 들어가 있는 형태를 말한다.
#중요하게 기억해야할 것은 내부 반복문은 외부 반복문이 한 번 반복할 때마다 새롭게 실행해야 된다는 점이다.

for y in range(5):
    for x in range(10):
        print("*",end="")
    print("")
    
for y in range(5):
    for x in range(y+1):
        print("*",end="")
    print("")
    
    
    
#format 함수 이용
print("정수값:{},   string:{},  float:{}".format(10,"안녕하세요",10.01))
#(:)을 기준으로 우측에 > 혹은 < 부등호를 사용해서 방향을 지정해줄 수가 있다.
print("숫자 '{:>5d}'".format(300)) #오른쪽(>)으로 밀어서 출력
print("숫자 '{:<5d}'".format(300)) #왼쪽(<)으로 밀어서 출력
for i in range(5):
    print("{:<5}".format("*"*(i+1)))
    
    
print("------------------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
    
print("------------------------------------")
    
for i in range(6,0,-1):
    print("{:<5}".format("*"*(i-1)))