#grade모듈 만들기

#아래 함수는 사용자로부터 성적을 입력받는다.
#음수를 입력받으면 멈춘다.

def readList():
    scoreList = [] #성적 저장할 리스트 타입의 변수 선언
    flag = True
   
    while flag:
        score = int(input("성적을 입력하세요(종료를 하시려면 음수를 입력) :"))
       
        if score < 0:
            flag = False
        else:
            scoreList.append(score)
            
    return scoreList


#입력받은 성적의 오름차순으로 정렬하는 함수
def sortingList(scoreList):
    scoreList.sort()
    return scoreList

#출력함수
def show_score(scoreList):
    j =0
    for i in scoreList:
        print(j,": ",i)
        j+=1