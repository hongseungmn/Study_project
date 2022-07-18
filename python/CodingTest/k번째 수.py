def solution(array, commands):
    answer = []
    for item in commands:
        #answer.append(sorted(array[item[0]-1:item[1]])[item[2]])
        answer.append(sorted(array[item[0]-1:item[1]])[item[2]-1])
        
    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = solution(array,commands)
print(answer)

