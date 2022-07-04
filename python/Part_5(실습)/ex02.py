#학생들의 성적을 처리하는 프로그램을 만들기
student_score=[]
avg = 0
best_student_num = 0
best_student =[]
hap =0

flag = True
while flag == True:
    name = input("이름 입력")
    score = int(input("성적 입력"))
    if score ==-1:
        flag = False
        avg = hap / len(student_score)
    else:
        student_score.append([name,score])
        if score >=80:
            best_student_num +=1
            best_student.append(name)
        hap += score
    
print(avg,best_student_num)
print(best_student)
print(len(student_score))


#리스트는 다양한 데이터를 저장할 수 있다.
#하지만 현업에서는 같은 종류(모델)의 같은 타입의 데이터를 저장하면서 사용한다.

#리스트는 문자열도 저장할 수가 있다.

dog_name = []
flag = True
while flag:
    name = input("name of dog")
    if name == '':
        flag = False
    else:
        dog_name.append(name)
        

print(dog_name)