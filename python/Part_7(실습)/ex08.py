#문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램

def main():
    string = input("문자열을 입력하세요 : ")
    dic1 = {"alphas":0, "digits":0, "spaces":0 }
    
    for i in string:
        #알파벳이라면...
        if i.isalpha():            
            dic1["alphas"] +=1
        elif i.isdigit():
            dic1["digits"] +=1
        elif i.isspace():
            dic1["spaces"] +=1
    print(dic1)
    
if __name__ == "__main__":
    main()