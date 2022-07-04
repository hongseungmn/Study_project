#사용자로부터 달을 입력받아서 입력한 달의 일수를 구하는 프로그램
month = int(input("월을 입력하세요:"))

if month == 2:
    print("월의 일수는 28일")
elif(month==4) or (month==6) or (month==9) or (month==11):
    print(30)
else:
    print(31)
    
#사용자로부터 연도를 입력받고 윤년인지 아닌지를 판단하는 프로그램을 만들기
year = int(input("연도를 입력하세요"))

