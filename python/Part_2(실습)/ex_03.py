#부울(bool) 변수 알아보기
#부울 변수의 영도는 플래그 변수 형태로 사용을 많이 한다.
#타 프로그래밍 언어에서는 부울 변수의 값은 소문자로 시작하는 true,false를 사용하지만
#파이썬은 대문자로 시작

flag =  not True
#파이썬에서 부울 변수의 값을 바꾸기 위해서는 not연산자를 이용하면 된다.
if flag:
    print("go")
else:
    print("error")
    
#블록의 중요성에 대한 실습
#타 언어에선 {} 으로 표현
