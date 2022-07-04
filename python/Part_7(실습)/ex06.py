#str 클래스의 메서드 실습
#split() : 문자열에서 단어(토큰)을 분리하고자 할 때 사용하는 메서드이다.
#인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열을 분리한다.
#기본 인자값 공백이다.
string = "안녕 john 난 지금 학교가고 있어"
li1 = string.split() #공백으로 분
print(type(li1))
print(li1)

#split()구분자를 하나만을 가진다.
#정규 표현식을 사용하기 위해 regex 모듈을 install
string = "안녕,john,난,지금,학교가고,있어"
li1 = string.split(',') #공백으로 분리
print(type(li1))
print(li1)

#문자열을 검사
string = "abcd"
print(string.isalpha()) #문자열이 영문자인지 확인하는 코드

string = "12345"
print(string.isdigit()) #문자열이 숫자인지 확인하는 코드
print(string.isdecimal()) #문자열이 10진수인지 확인하는 코드

string = "abcd1234"
print(string.isalnum()) #문자열이 영문자, 숫자인지 동시에 확인하는 코드

string = "1.2" 
print(string.isnumeric()) 
# numeric은 굉장히 넓은 의미로, 숫자값 표현에 해댕하는 문자열을 확인해준다.
#str클래스에서 음수, 실수 판별하는 메서드는 없다.

string = " " 
print(string.isspace()) #공백인지 확인하는 것

#부분문자열 검색 실습
string = input("파이썬 소스를 입력해주세여 : ")
#endswith(문자열) 메소드는 인자값 문자열로 끝이 나면 True리턴한다.
if string.endswith(".py"):
    print("올바른 파일이름입니다.")
else:
    print("틀린 파일이름입니다.")
    

#startswith(문자열) 메소드는 인자값이 문자열로 시작하면 True리턴한다.
string = "2022년 데이터 입니다."
if string.startswith("2022"):
    print("2022년 파일입니다.")
else:
    print("2022년 파일이 아닙니다...")
    
string = input("영어 단어를 입력하세요 : ")
print(string.upper())       #대문자로 변경
print(string.lower())       #소문자로 변경
print(string.capitalize())  #앞 한글자만 대문자로 변경
print(string.title())       #앞 한글자만 대문자로 변경

#format()는 포맷 {}을 만들어 놓고 문자열을 생성하는데 사용하는 것이다.
string = "{}b{}"
print(string.format("a","c"))

#join()는 리스트 값은 반복(iterable)인자를 전달 받아서 문자열로 연결하는데 사용
string = ["a","b","가"]
print("!".join(string))

#partition()는 전달단은 인자값으로 문자열을 나눈다. 리턴 타입은 튜플이다.
string = "sem50000@naver.com" 
print(string.partition("@"))

#count()는 인자값으로 들어오는 값을 문자열에서 몇 개 있는지 카운팅을 해준다
#찾는 인자값이 없다면 0을 리턴해준다.
string = "aaaaaabc" 
print(string.count("z"))

#find()메서드는 특정 단어를 찾아서 인덱스를 리턴하고 없다면 -1을 리턴한다.
#index() 차이점은 특정 단어를 찾으면 인덱스를 리턴하지만 없다면 에러를 발생시킨다.
string = "apple"
print(string.find("p"))
print(string.index("p"))

#문자열에서 공백을 제거하는 방법
#strip(): 양족 공백 제거, 탭문자, 줄바꿈(enter)도 제거
#lstrip() : 왼쪽 공백만 제거(탭키 포함)
#rstrip() : 오른쪽 공백만 제거(탭키 포함)
#단 메소드로 문자열 중간에 존재하는 공백은 제거할 방법이 없다(함수를 만들어서 직접 사용해야 한다.)

string = "          aaaaa   bbbbb   cccccc ddddd            \t"
print(string.strip())
print(string.rstrip())
print(string.lstrip())

