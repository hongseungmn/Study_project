#영한사전 만들기
#공백 딕셔너리 생성하고 영어단어를 키로하고 설명을 값으로 저장

word_list = {}

while True:
    menu = int(input("1.추가   2.검색   3.나가기"))
    if(menu == 1):   
        eng = input("영어를 입력하시오")
        kor = input("뜻을 입력하시오")
        word_list[eng] = kor
    elif(menu == 2):
        print(word_list)
        find_word = input("검색할 단어 입력")
        if find_word in word_list:
            print(word_list[find_word])
        else:
            print("사전에 없는 단어입니다")
    elif(menu == 3):
        break;
    
            
        