#문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.    
# first_name = "eun Hyuk"
# last_name = "Shin"
# name = last_name + first_name
# print(name)

# #파이썬에서는 모든 데이터에는 데이터 타입이 존재한다.
# #아래 소스코들에서 확인을 하면 "Person"은 문자열이고, 100은 int타입이다.
# #하여 타입의 일치가 되지 않아 서로 연결을 하는데 에러가 발생한다.
# #temp = "Person" + 100
# #print(temp)

# temp = "Person" + str(100)
# print(temp)

# #문자열을 숫자로 변환
# price = int("123456")
# print(type(price))
# print(price)

# price = float("123.456")
# print(type(price))
# print(price)

#문자열의 반복
#문자열에서 *연산자를 사용하면 그만큼 반복이 된다.
arrow = "->" * 10
print(arrow)

#형식 지정자(%s)
price = 1000
print("가격 : %s" % price )
