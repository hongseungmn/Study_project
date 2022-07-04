#논리 연산자(logical operator)는 두 개 이상의 조건을 조합해서 참인지 거짓인지 판단
name ="신은혁"
age = 14
height = 160

#and 논리 연산자는 여러 개의 조건 중에서 처음 조건이 거짓이라면 다른 조건은 전혀 검사조차 하지 않는다.
#and 논리 연산자는 모든 조건이 참일 시 참을 반환한다.
if(age==14) and (height >=160) and (name=="신은혁"):
    print("탑승 가능")
else:
    print("탑승 불가")


print("---------------------------------------")


#or 연산자
#or 논리 연산자는 모든 조건 중에서 하나만 참이면 참을 반환을 한다.
if(age >= 14) or (height >= 160) or (name == "신은혁"):
    print("탑승 가능")
else:
    print("탑승 불가")
    
print("---------------------------------------")

#논리부정 연산자인 not에 대한 실습
#논리부정 연산자인 not은 조건이 참이면 전체 조건식의 결과를 반대로 거짓으로 만들고
#조건식의 결과가 거짓이라면 참으로 바꾸는 역할을 한다.
if not(1==0):
    print("참입니다")   
else:
    print

#대학교를 졸업하려면 적어도 140학점을 이수해야 하고 평점은 2.0은 되어야 한다고 해보자. 이것을 프로그램으로 만들어보자

point = int(input("이수 학점을 입력하세요"))
score = float(input("평점을 입력하시오"))

if point >=140 and score>=2.0:
    print("Graduate")
else:
    print("not Graduate")
    
#몸무게와 키를 입력받고 BMI가 20.0이상이고 25미만이면 표준 아니면 체중관리 필요 출력
#BMI = 몸무게 / 키^2

height = float(input("키를 입력:"))
weight = float(input("몸무게를 입력:"))

height /= 100.0
BMI = weight / (height**2)

if not(BMI>=20 and BMI <25):
    print("체중 관리가 필요")
else:
    print("정상입니다.")