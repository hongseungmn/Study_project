#자동 판매기를 시뮬레이션하는 프로그램을 작성하는데 사용자는 1000원짜리 지폐와
#500원, 100원짜리 동전을 사용할 수 가 있다. 물건값을 사용자로부터 입력을 받아서 
#1000원 지폐, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산
#하여서 동전으로 반환하는 프로그램을 만들어보자

itemPrice = int(input("물건 값을 입력하세요 : "))
bills_1000 = int(input("1000원 지폐 개수 : ")) 
coin_500 = int(input("500원 동전 갯수 : "))
coin_100 = int(input("100원 동전 갯수 : "))

#거스름돈 구하기
nod_money = ((bills_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - itemPrice

change_1000 = nod_money // 1000
nod_money = nod_money % 1000

change_500 = nod_money // 500
nod_money = nod_money % 500

change_100 = nod_money//100

print('거스름돈은 1000원 :{0}, 500원 :{1}, 100원 :{2}'.format(change_1000,change_500,change_100))