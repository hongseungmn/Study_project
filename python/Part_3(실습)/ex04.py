#사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

num = int(input("출력하고 싶은 단을 입력하시오"))

for i in range(1,10,1):
    if num < 2 or num >9:
        print("단을 잘못 입력하셨습니다")
        break
    print(num," * ",i,"=",num*i)
    
#사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터 두 번째 입력받은 값까지의
#범위에서 3의 배수이고 4의 배수를 제외하고 출력하는 프로그램을 작성하시오

n1 = int(input("첫 번째 수: "))
n2 = int(input("두 번째 수: "))
for i in range(n1,n2+1):
    if (i%3==0) and (i%4==0):
        continue # 조건식이 참이면 아래 문장을 실행하지 않고 다음 for문으로 이동
    print(i,end=" ")
    
import turtle
t = turtle.Pen()

for i in range(5):
    t.forward(50)
    t.right(145)
    

turtle.exitonclick()