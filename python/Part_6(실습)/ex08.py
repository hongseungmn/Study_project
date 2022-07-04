data_list = [(90,80),(85,75),(90,100)]

#enumerate()함수의 역할 : 반복문 사용 시 몇 번째 반복을 확인할 때 사용을 한다.
for i,scores in enumerate(data_list):
    #print(i,score)
    #학생 1명씩 점수를 누적시킴
    hap = 0
    for score in scores:
        hap += score
    print("%d번 학생의 총점은 %d이고, 평균은 %0.1f입니다." % (i+1,hap,hap/2.0))