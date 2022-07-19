# 내장 함수에 대한 실습

print("------>>>>> abs()")
# abs() : 절대값을 반환
i = -20
print("i의 절댓값 : ",abs(i))
i = -20.55
print("-20.55의 절대값 : ",abs(i))


print("------>>>>> all()")
# all() : 시퀀스(리스트, 딕셔너리 등)을 받아서 시퀀스의 모든 항목이 참이면 True를 반환한다
# and 조건과 유사하다. 하나라도 0인 값이 들어가면 False를 리턴한다.
list1 = [1,4,7,10] # 모든 값이 참이다
print(all(list1))
list2 = [1,4,0,10] # 0은 거짓이다
print(all(list2))


print("------>>>>> any()")
# any() : 시퀀스 객체에 있는 한개의 항목이라도 참인 경우에 참을 반환한다
# or 개념과 유사하다
list1 = [0,7,10,20] # 1개의 값이 False이므로 True 리턴
print(any(list1))
list2 = [0,0,0,0]    # 모든 값이 False 이므로 False 리턴
print(any(list2))


print("------>>>>> bin()")
# bin() : 10진수를 이진수로 표현해주는 함수, 항상 접두사 0b로 시작한다
y = bin(15)
print(y)


print("------>>>>> eval()")
# eval() : 전달된 수식을 구문 분석을 하고, 프로그램 내에서 수직의 값을 계산하는 함수
# eval() 는 전역 변수의 수식도 구문을 분석해서 계산해준다
exp = input("수식을 입력해주세요 : ")
print(eval(exp))
x = 10
y = 15
print(eval("x*y"))


print("------>>>>> sum()")
# sum() : 리스트에 존재하는 항목들의 값을 전부 더하여 합계를 리턴
print(sum([1,10,100]))



print("------>>>>> len()")
# len() : 객체의 길이를 반환하는 함수, 문자열의 길이를 계산하는데 유용하다
# 리스트에 len() 사용하게 되면 리스트 안에 있는 항목의 개수를 리턴
# 딕셔너리, 튜플에서도 항목의 개수를 반환
print(len("안녕하세요, hello!!!"))
print(len[1,2,3,4,5,6,7])
dic = {
    "a" : 7,
    "b" : 10,
    "c" : 15,
}
print(len(dic))
tup = (2,7,5,4,2)
print(len(tup))


print("------>>>>> list()")
# list() : 리스트를 생성하는 함수이다
s = "abacads"
print(list(s))
