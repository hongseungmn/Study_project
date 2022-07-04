#2차원 리스트에 대한 실습
double_list = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
]
print(double_list[0])
print(id(double_list[0]))
print(len(double_list[1]))
print(id(double_list[2]))

#2차원 리스트의 출력을 하려면 반드시 더블루프를 사용해야 한다.
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j],end="\t")
    print()
    
#2차원 리스트는 정적인 것보다는 동적으로 생성하여 사용하는 경우가 많다
rows = int(input("원하는 행을 입력해주세요 : "))
cols = int(input("원하는 열을 입력해주세여 : "))
dbl_list = []
for row in range(rows):
    dbl_list +=[[0] * cols]
print(dbl_list)

#리스트 함출을 이용한 방법
dbl_list = [([0]* cols)for row in range(rows)]

#1차원 리스트에서는 list1[0]값이 바로 변수와 동일하다.
#2차원 리스트에서는 list2[1][1]값이 바로 변수와 동일하다
li1 = [1,2,3]
li1[0] = 10 #1차원 리스트에 값을 저장하는 형태

li2 = [[1,2],[3,4]]
li2[0][1] = -7
print(li2)
