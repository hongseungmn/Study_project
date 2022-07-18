# 파이썬에서 파일을 읽는 방법
# read(), readline(), readlines() 함수를 사용하여 파일을 읽는다.
# read() : 모든 파일의 내용을 읽어들인다.
# readline() : 한 번에 한 번씩 읽어들인다.(for 문을 함께 사용한다,)
# readlines() : 여러 라인을 리스트에 저장한다. 기본적으로 빈칸(개행, \n)이 포함된다.

# read()로 test.txt를 읽는 방법
print("1. read()함수 읽기")
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","r")
string = file.read()
print(string)
file.close()

# readline()로 test.txt를 읽는 방법
print("2. readline()함수 읽기")
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","r")
string = file.readline().rstrip()
while string != "":
    print(string)
    string = file.readline().rstrip()
file.close()

# readlines()로 test.txt를 읽는 방법
print("3. readlines()함수 읽기")
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/test.txt","r")
list = file.readlines().rstrip()
print(type(list))
#string = ''.join(list)
print(list)
file.close()