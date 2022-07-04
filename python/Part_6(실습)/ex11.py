#두 개의 세트에 있는 사람 이름 중에 2개의 파티에 모두 참석한 사람은 누구인가를 출력하시오
partyA = set(["신은혁","김연아","손연재","김철수"])
partyB = set(["최양락","김기훈","손연재","안철수"])

both_party = set(partyA.intersection(partyB))
print(both_party)

#텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를 계산



#단어에서 마침표를 제거하고 소문자로 만드는 함수
def process(word):
    out_str = ""
    for ch in word:
        if ch.isalpha(): #영문자라면 ...
            out_str += ch
    return out_str.lower() #단어를 소문자로 리턴해준다.
            
if __name__ =="__main__":
    words = set() #비어있는 set를 만든다
    f_name = input("입력파일 이름 : ")
    file = open('./words.txt',mode="r") # 파일을 열고 읽기모드로 설정
    
    #파일의 모든 줄에 대해서 반복
    for line in file:
        linewords = line.split() # 한 라인을 읽어와서 단어(토큰)별로 분리하고 있다.
        for word in linewords:
            words.add(process(word))     #단어를 세트에 추가한다.