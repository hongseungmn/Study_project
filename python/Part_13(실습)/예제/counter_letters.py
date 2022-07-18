# 하나의 파일을 읽어서 그 안에 알파벳이 몇 개가 있는지 확인하는 프로그램
# counter = [0] * 26
# infile = open("/Users/hongseongmin/Documents/GitHub/Study_project/python/Part_13(실습)/예제/counter_letters.py")
# ch = infile.read(1)
# while ch != "":
#     ch = ch.upper() # 대문자로 바꾼다
#     #알파벳이라면....
#     if ch >="A" and ch <="Z":
#         # ord()는 유니코드를 반환 ,A를 빼면 현재 알파벳의 문자번호를 알 수가 있다.
#         i = ord(ch) - ord("A")
#         counter[i] += 1
#     ch = infile.read(1)
    
# print(counter)

# 사용자로부터 파일 안에 문자들의 개수를 세는 프로그램을 작성하기
filename = input("파일명을 입력하세요 : ").strip()
infile = open(filename,"r")

freqs = {}
for line in infile:
    for char in line.strip(): # 문자들의 양쪽 공백을 제거
        if char in freqs:
            freqs[char] +=1 # 문자 하나를 누적
        else:
            freqs[char] = 1 # 제일 처음 나왔을 때
            
print(freqs)
infile.close()



infile.close()