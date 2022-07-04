#기본적인 파일 입출력 실습
from statistics import mode

data = []
#파일의 경로를 지정하고 읽기 모드로 문자셋 UTF-8로 설정해서 해당 파일을 열고 메모리에 로딩된 파일의 주소를 반환한다.
fp = open("파일 절대 경로 작성",mode="r",encoding="UTF-8")

#readlines() 메서드는 파일의 저장된 내용을 한번에 다 읽는다.
for line in fp.readlines():
    #strip() 메서드는 원래 문자열의 양쪽 공백을 제거하는 역할을 하지만,
    #파일을 읽어들일 때는 엔터키 제거를 해준다.
    print(line.strip())
    data.append(line.strip())
#프로그램에서 리소스를 다 사용했으면 반드시 close()메서드를 호출하도록 한다.
print(data)
fp.close()

#파일에 내용을 작성하는 방법
#파일의 모드가 w인 경우에는 기존 파일의 내용을 덮어써버린다.
fp = open("파일의 절대 경로",mode="w",encoding="UTF-8")
fp.write("우리는 파이썬을 공부합니다")
fp.write("저희도 파이썬을 공부합니다")
fp.close()

#기존 파일의 내용에 추가를 한다. 
fp = open("파일의 절대 경로",mode="a",encoding="UTF-8") # mode=a로 한다.

#csv파일 읽는 방법
import csv
fp = open("파일의 절대 경로",mode="r")
reader = csv.reader(fp)
print(reader)
for txt in reader:
    print(txt)