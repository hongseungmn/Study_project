# 파일에 쓰기 실습

# open()는 모드가 읽기 모드는 파일이 없으면 FileNotFoundError가 발생한다.
# 하지만 모드를 쓰기,추가 모드로 바꾸면 새로운 파일을 생성한다.
file = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/test2.txt","w")

file.close()