#리스트에 대한 실습
#리스트의 정의:대량의 데이터를 저장할 수 있는 공간을 만들어야 하고 이 데이터들을 
#손쉽게 처리할 수 있는 형태의 데이털의 저장 구조를 의미한다.


#리스트를 선언 및 초기화
scores = []
print("리스트 초기화 값",scores)

scores.append(30)
scores.append("안녕")
scores.append(10.223242)
print("리스트에 요소 추가",scores)
print(len(scores))


#리스트의 값을 변경해보기
scores[0] = "hello"
print(scores[0])

#리스트 순회해서 출력하기
for i in range(len(scores)):
    print(scores[i])
    
#시퀀스를 사용하면 인덱스를 가져오는 것이 아니라, 실제 값을 가져와서 출력한다.

#list 클래스(속성(매개변수),기능(멤버메서드),생성자) 생성자를 이용한 리스트 만들기
li1 = list() # 매개변수가 없는 생성자를 호출
print(li1)

#아래와 같이 생성자의 매개변수가 문자열이라면 리스트를 생성할 때 문자 하나하나씩 요소로 가지게 된다.
li2 = list("안녕")
print(li2)

li3 = list(range(0,5,2))
print(li3)

#내장 리스트에 대한 실습
li1 = [12,12.777,"안녕"]
li2 = [["서울",10],["뉴욕",50],["파리",70]]

print(li2[0][0],li2[0][1])

#내장 리스트를 더블 루프로 출력하기
for i in range(len(li2)): # len(li2) = 3
    for j in range(len(li2[i])): # len(li2[i]) = 2 
        print(li2[i][j]) # 2중 내장 리스트는 li[i][j]은 곧 변수와 동일하다.
        
        