#성적 처리 프로그램 만들기(2차원 리스트를 이용)
#주어진 성적
# score = [
# [100,100,100],
# [20,20,20],
# [30,30,30],
# [40,40,40],
# [50,50,50]]

row = int(input("열을 입력하시오"))
col = int(input("행을 입력하시오"))
score_num = [([0]*(row+1)) for i in range(col+2) ]
print(score_num)
score_num =[
[100,100,100,0,0],
[20,20,20,0,0],
[30,30,30,0,0],
[40,40,40,0,0],
[50,50,50,0,0]] 


def printList(li):
    for i in range(5):
        for j in range(5):
            print(li[i][j],end=" ")
        print()
        
def init(li):
    row_sum =0
    row_in=0
    for i in range(5):
        row_sum += li[i][row_in]
        row_in +=1 
        
        col_sum=0
        col_avg=0
        for j in range(5):
            col_sum +=li[i][j]
        li[i][3] = col_sum
        li[i][4] = col_sum // 3

printList(score_num)
init(score_num)
printList(score_num)