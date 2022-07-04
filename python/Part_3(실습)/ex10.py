#소수를 2부터 계속 더할 때, 2000까지 합은 얼마이고,
#마지막으로 더해지는 소수는 얼마인지 출력하는 프로그램을 작성

start_num =0
num =0
sum =0
last_num = 0

for num in range(2,2001,1):
    for start_num in range(2,num+1):
        #배수이거나 소수인지를 걸러내는 조건식
        if num%start_num == 0:
            break
    #아래 조건이 참=> 자기자신으로 나눠서 나머지가 0이 나왔다는 것은 소수를 의미한다.
    if num == start_num:
        print("소수: ",start_num)
        sum += start_num
        print("합계: ",sum)
        last_num = start_num
        print("마지막 소수의 값: ",last_num)