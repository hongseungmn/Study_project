#탐색하기
#주어진 데이터 내에서 어떠한 특정한 값을 찾는 행위가 탐색하는 것이다.
#index()를 이용하여 일반적인 탐색이 가능하다
list_word = ['gold','blue','red','yellow','green']
search_word = input("찾고자 하는 단어를 입력해주세요 : ")

if search_word in list_word:
    index = list_word.index(search_word)
    print("찾고자 하는 단어가 ",index,"인덱스에 존재합니다.")
else:
    print("찾고자 하는 단어가 없습니다.")
#프로그래머가 직접 탐색을 하는 알고리즘
#탐색의 가장 기본적인 방법이 순차 탐색이다.
#순차 탐색은 리스트의 요소를 순서대로 하나씩 꺼내어 탐색키 값과 비교해서 성공하면
#루프를 빠져나오고 루프를 다 했음에도 없다면 탐색키가 존재하지 않음을 의미한다.
cnt = 0
def number_search(list,key):
    for i in range(len(list)):
        if key == list[i]:
            cnt += 1    #함수에 같은 값이 존재하면 증가
    return cnt

#같은 수가 존재한다면 그 갯수도 몇 개인지 출력하시오
num_list = [10,20,30,40,50,60,70,80,90,100]
key = int(input("찾고자 하는 정수를 입력하세요 : "))
return_value = number_search(num_list,key)

if return_value == 0:           #cnt가 0이라면 찾고자 하는 값이 존재하지 않는다
    print(key,"은 존재하지 않습니다")
else:                           
    print(key,"은",return_value,"개 존재합니다")
    
    
#모든 조건에 만족하는 항목을 전부 출력하는 코드
result = []

for i in num_list:
    if i >= 50:
        result.append(i)

print(result)
