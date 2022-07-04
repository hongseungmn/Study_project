#쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면 5%의 할인을 해준다고 하자. 
#사용자에게 구입 금액을 입력받고 최종적으로 할인 금액과 지불 금액을 출력하는 프로그램 만들기

total_price = int(input("구입 금액을 입력하세요:"))
if total_price >=50000:
    discount = total_price*0.05
    sales_price = total_price - discount
    print(total_price)
    print(discount)
    print(sales_price)
else:
    print("할인 금액 대상이 되질 않습니다",(50000 - total_price),"만큼 더 구매하시오")
    
    
#문자열의 중앙에 있는 문자를 추출해서 출력을 하는 프로그램 만들기

str_1 = input("단어를 입력하십시오")
str_len = len(str_1)
if str_len % 2 == 0:
    print("문자열의 갯수가 짝수입니다")
else:
    center_str = str_1[str_len//2]
    print(center_str)
