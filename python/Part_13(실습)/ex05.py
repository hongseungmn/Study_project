# 파이썬에서 파일 쓰는 방법
# write() : 빈칸(\n)이 필요하면 직접 입력해야 한다.
# writelines() : 리스트 등으로 된 여러 문장을 입력하기 위해서 사용한다.
# 문자열을 빈칸(\n)으로 연결하기 위해 join()을 사용한다.

print("1. write() 사용")
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","w")
file.write("안녕하세요 반갑습니다\n")
file.write("저는 홍길동입니다\n")
file.close()

print("2. writelines() 사용")
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","a")
# 리스트 형태로 바로 파일에 기록했다.
file.writelines("\n".join(["하나","둘","셋","넷","다섯","화이팅!"]))
file.write("\n")
file.close()