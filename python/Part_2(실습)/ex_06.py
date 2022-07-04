#if ~ elif ~ else(옵션) 대한 실습

score = int(input("성적을 입력하세요(0~100):"))

if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else: #else 구문은 옵션이지만 다중 조건을 설정할 때는 절대 조건을 명기하면 안된다.
    print("학점 F")