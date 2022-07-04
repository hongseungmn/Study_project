#입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 코드

statements = input("원하는 문자열을 입력하세요: ")
result = ""

for ch in statements:
    if ch != " ":
        result += ch


print("입력한 문자열",statements)
print("공백을 제거한 문자열",result)

print("")
print("---------------------------------------------")

#입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오
statements = input("문자열을 입력하세요:")
revers_statements = ""

for ch in statements:
    revers_statements = ch + revers_statements
    
print("입력한 문자열:",statements)
print("역순으로 출력한 문자열:",revers_statements)


s_list = list(statements)
#print(type(s_list))
#reverse()는 리스트 타입을 역순으로 바꿔주는 함수이다.
s_list.reverse()
#join() 함수는 역수능로 된 문자열을 연결해서 출력을 하고있는 코드 
print("s_list: ".join())# 각 원소를 연결

print("")
print("---------------------------------------------")
print(statements[::-1])
#문자열 3번째 인덱스부터 역순으로 출력하는 방법이다.
print(statements[::-1])