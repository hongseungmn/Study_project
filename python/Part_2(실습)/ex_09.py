#사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 대학생 분류

age = int(input("태어난 연도를 입력하시오"))

if(2022 - age <14):
    print("초등,유아")
elif(2022 - age < 17):
    print("중학생")
elif(2022 - age < 20):
    print("고등학생")
elif(2022 - age < 28):
    print("대학생")
else:
    print("일반인")
    
    
#중복(nested) if ~ else 구문
#사용자로부터 아이디를 입력받아 등록되어진 아이디인지를 검사하는 프로그램 작성

id = input("아이디를 입력하시오")
pw = "1234"
user_list = ['신은혁','김연아','손연재','박길수']

if id in user_list:
    password = input("패스워드를 입력하시오")
    if password == pw:
        print(id+"로그인 하셨습니다")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("회원가입이 되질 않습니다")
