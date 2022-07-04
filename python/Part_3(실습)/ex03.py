#1부터 사용자가 입력한 수 num까지 더해서 합계를 구하는 프로그램을 for문을 이용해서 작성하시오
from re import I


sum = 0
num = int(input("what number still is odded  "))

for i in range(1,num+1):
    sum +=i
    
print(sum)

#1~100까지의 누적값을 구하는데 누적값이 2000이상이 되면 for문을 빠져 나오는 프로그램 작성
sum =0

for i in range(101):
    if sum>=2000:
        print(i)
        break
    else:
        sum += i
print(sum)

#for문을 이용하여 팩토리얼을 계산하는 프로그램을 작성해보자
num = int(input("n! n팩토리얼의 n을 입력:"))
fact=1
for i in range(1,num+1):
    fact *=i
print(fact)

#for문을 이용하여 피보나치 수열을 계산하는 프로그램 만들기 
# ->피보나치 수열 앞의 2개의 수를 더해서 다음 수를 결정짓는 수열

fibo = int(input("피보나치 n번째 수 입력:"))
n1= 1
n2= 1
n3= 1

for i in range(1,num):
    
    if i < 3:
        n3 =1
    else:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    
    if n3 < fibo:
        print(n3,end=" ")
    

    