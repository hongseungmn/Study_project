statements = "     안녕!"
#왼쪽 공백만 제거하는 함수
print(statements.lstrip())

#양쪽 공백만 제거하는 함수
statements = "          안녕   !        "
print(statements.strip())

#문자열을 토큰으로 나누기
statements = "나는 열심히 파이썬 공부를 합니다."    
print(statements.split())