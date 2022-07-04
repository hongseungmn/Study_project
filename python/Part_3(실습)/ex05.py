#while문의 실습
#while문은 조건을 정해놓고 반복을 하는 구조이다.

i=0
while i < 5:
    print("반갑습니다")
    i += 1
print("반복이 종료되었습니다")

i=0
while i <10:
    print(i,end=" ")
    i+=1
    
print("")
    
#while 문을 사용하여 3단을 출력하는 예제
i=0
while i <=9 :
    print("3 * %d = %d" %(i,i*3))
    i+=1


print("")
print("-------------------------------")
#정수 안의 각 자리수의 합을 계산하는 예제
num = int(input("수입력:"))
sum =0
while num>0:
    digit = num %10
    sum += digit
    num = num //10
print("입력받은 값으 자리수의 합은 %d이다"%sum)

