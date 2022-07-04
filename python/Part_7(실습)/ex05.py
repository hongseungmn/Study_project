#문자열에 대한 실습
#슬라이싱이란 것은 문자열에서 부분문자열로 만드는 잘라내는 작업을 의미한다.
word = "Python"
print(word)
word1 = word[0:3]
print(word1)
#파이썬에서는 슬라이싱에서 시작 인덱스나 종료 인덱스로 적절치 못한 값을 사용하더라도
#파이썬 인터프리터가 자동으로 적절한 값으로 변경하여 실행시켜준다.
print(word[0:200])

#문자열 비교하기(연산자)
print("apple" < "banana")
print(ascii("a파이썬"))
#ord()는 영문자를 아스키 코드로 출력해주는 함수
print(ord("b"))
#char()는 아스키 코드를 문자로 출력해주는 함수
print(chr(97))
print(chr(65))


#ascii()함수는 문자열이 알파벳이면 알파벳은 그대로 출력시켜주고
