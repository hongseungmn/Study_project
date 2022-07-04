# 머리 글자어(acronym): NATO(North Atlantic Treaty Organization)처럼
#각 단어의 첫 글자를 모아서 만든 문자열이다. 사용자로부터 문자를 입력하면 해당되는 머리 글자어를 출력하는 프로그램

# def acro(string):
#     list =[]
#     list.append(string[0])
#     for i in range(len(string)):
        
#         if string[i].isspace():
#             list.append(string[i+1])
    
#     for i in range(len(list)):
#         print(list[i].upper(),end="")
#     return list

# if __name__ =="__main__":
#     string = input("문자열을 입력하시오: ")
#     acro(string)

            
            
def main():
    string = input("문자열을 입력하시오 : ")
    acronym =""
    #입력받은 문자열을 대문자로 변환 후, 문자열을 분리
    for word in string.upper().split():
        acronym += word[0]
        
    print("머리 문자열 : " + acronym)

if __name__ =="__main__":
    main()