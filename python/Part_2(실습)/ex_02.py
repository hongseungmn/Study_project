#조건문 if 구문만 사용
score = 63
#많은 if 구문이 존재하더라도, CPU는 모든 if문을 참조한다
#그러므로 애플리케이션 프로그램의 성능이 저하된다.

if score >= 90:
    print("A++")
if score >= 80:
    print("B++")
if score >= 70:
    print("C++")
if score >= 60:
    print("D++")
    
#사용자로부터 성별을 입력받아 해당하는 성별을 출력하는 프로그램 만들기

gender = input("write gender")
# 조건이 딱 절반(50%)일 경우에 사용한다.
if gender =="man":
    print("man")
else:
    print("male")
    
