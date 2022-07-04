#사용자로부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후
#출력하는 프로그램을 작성해보시오. 단, 센티널은 음수의 값을 사용하시오


count =0
score =0
sum =0
cnt =0
avg =0
count = int(input("개수를 입력하시오"))
while count>=0:
    score = int(input(str(cnt+1)+"성적을 입력하시오"))
    if score >=0:
        sum +=score
        cnt +=1
    count -= 1
    
if cnt > 0:
    avg = sum/count

print("합계: ",sum," 평균: ",avg)
    
   
#임의의 숫자를 발생시켜 숫자를 맞추는 게임
from random import *
cnt = 0
num = randint(1,100)
print("발생한 난수의 값 : ",num)

print("1부터 100사이의 숫자를 맞추어 보세요")
print("기회는 단 10번입니다.")

while cnt < 10:
    guess = int(input("예상되는 숫자를 입력하세요"))
    cnt += 1
     
    if guess < num:
        print("입력한 수가 난수보다 작습니다.")
    elif guess > num:
        print("입력한 수가 난수보다 큽니다.")
    elif guess == num:
        print("정답입니다.", cnt)
        break
        