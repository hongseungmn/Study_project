appleQuality = input("사과의 상태를 입력하시오(좋음, 나쁨) : ")
applePrice = int(input("사과 1개당 가격을 입력하세요 : "))

if appleQuality =="좋음":
    if applePrice < 1000:
        print("10개를 산다")
    else:
        print("5개를 산다")
else:
    print("사과를 사지 않는다")
    
#사용자로부터 정수를 입력받아서 음수,0,양수 중에 어떤 값인지를 출력하는 프로그램

num = int(input("정수를 입력하시오 : "))

if num > 0:
    print("양수입니다")
elif num==0:
    print("0입니다")
else:
    print("음수입니다")
    
