#사용자가 지정하는 파일을 읽어서 파일에 저장되어진 각각의 단어가 몇 번이나 나오는지 계산
f_name = input("파일 이름 입력 : ")
file = open(file=f_name,mode="r",encoding="UTF-8")

word_count = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] +=1
            
print(word_count)