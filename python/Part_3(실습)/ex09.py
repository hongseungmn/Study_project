

for y in range(5):
    #print("{:>10}".format("*"*(y+1) + "*"*y))
    print(" "*(4-y) + "*"*(2*y+1))

print("-------------------------------")
#1. 더블루프 사용
for i in range(1,6):
    #공백을 찍는 내부 루프
    for j in range(5-i):
        print(" ",end="")
    #별표를 찍는 부분
    for j in range(1,i*2):
        print("*",end="")
    #줄바꿈
    print("")
    
    
print("-------------------------------") 
#2. format() 사용
for i in range(1,11,2):
    #^는 중앙정렬을 할 수 있다.
    print("{:^10}".format("*"*i))
    
    
print("-------------------------------")
#상단의 삼각형 부분을 출력
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print("")

for i in range(6):
    for j in range(i):
        print(" ",end="")
    for j in range(10,(i*2)+1,-1):
        print("*",end="")
    print("")

