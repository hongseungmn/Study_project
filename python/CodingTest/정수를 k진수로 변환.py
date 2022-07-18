# 정수를 k진수로 변환하기


def trans(num,k):
    numa =""
    while(num >0):
        num,mod = divmod(num,k)
        numa += str(mod)
        
    return numa[::-1]

def solution(n, k):
    if(k==1 | n==0):
        return -1
    numa = trans(n,k)
    from posixpath import split
    numb = numa.split('0')
    numb = list(numb)
    numc = []
    for i in numb:
        if( i == ""):
            continue
        numc.append(int(i))
    numd = []
    for i in numc:
        flag = False
        for j in range(2,i//2,1):
            if((i % j) == 0):
                flag = True
                break
        if((flag == False) & (i !=1)):
            numd.append(i)
    answer = len(numd)
    return answer


# from posixpath import split


# def trans(num,k):
#     numa =""
#     while(num >0):
#         num,mod = divmod(num,k)
#         numa += str(mod)
        
#     return numa[::-1]

# num = 110011
# numa = trans(num,10)
# print(numa)
# print(type(numa))
# numb = numa.split('0')
# print(numb)
# numb = list(numb)
# numc = []
# for i in numb:
#     if( i == ""):
#         continue
#     numc.append(int(i))
# numd = []
# print(numc)

# for i in numc:
#     flag = False
#     for j in range(2,i//2,1):
#         if((i % j) == 0):
#             flag = True
#             break
#     if((flag == False) & (i !=1)):
#         numd.append(i)
            
# print(numd)
        
# answer = len(numd)