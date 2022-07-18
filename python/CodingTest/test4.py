# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

def solution(absolutes, signs):
    list_a = []
    for i in signs:
        i = 1 if i==True else -1
        list_a.append(i)
    print(list_a)
    
    product = [x*y for x,y in zip(absolutes,list_a)]
    return sum(product)
        
absolutes = [4,7,12]
signs = [True,False,True]
answer = solution(absolutes,signs)
print(answer)
