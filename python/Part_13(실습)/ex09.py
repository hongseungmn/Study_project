import csv

f = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/alphabet.txt","r")
data = csv.reader(f)
header = next(data) # 헤더 제거하기
temp = 1000

for row in data:
    if temp > float(row[3]): #최저 기온은 3번 인덱스에 위치하고 있다.
        temp = float(row[3])
        
print("가장 추웠던 온도는 ",temp,"입니다. ")
