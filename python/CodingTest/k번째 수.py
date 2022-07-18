def solution(array, commands):
    answer = []
    list_a = []
    for item in commands:
        list_a = array[item[0]:item[1]]
        
        list_a = list_a.sort()
        answer.append(list_a[item[2]])
    
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array,commands)