#사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기

from operator import __eq__

sum =0
while True:
    price = input("상품 금액을 입력:")
    
    # if price =="끝":
    #     break
    # else:
    #     sum += price
    
    if __eq__(price,"끝"):
        print("total",sum)
        break;
    else:
        sum += int(price)
        
        

#1.증속, 2.감속, 3.중지 를 출력하고 사용자의 입력을 1,2,3 받아서 
#증속을 하면 속도를 10씩 증가하고 출력


speed=  0
run = True
keyCode =0
while run:
    print("-----------------------------")
    keyCode = input("1.증속   2.감속  3.중지")
    
    if keyCode == '1':
        speed += 10
    elif keyCode == '2':
        speed -= 10
    elif keyCode == '3':
        print(speed)
        run = False
    else:
        print("잘못된 입력값입니다")
        

print("프로그램 종료")

    