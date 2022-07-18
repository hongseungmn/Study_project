# 파이썬 파일 현재 위치 확인 및 변경을 하는 실습
# tell() : 파일의 현재 위치를 확인할 때 사용한다.
# seek() : 파일 현재 위치를 변경할 때 사용한다.
# seek(0) : 파일의 처음 위치로 돌아간다

file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","r")
print("파일포인터의 현재 위치 : ", file.tell())
print(file.read())
print("파일 포인터의 현재 위치 : ",file.tell())


print("-----------------------------------------------")
file.seek(0) # 맨 처음 위치로 포인터를 이동