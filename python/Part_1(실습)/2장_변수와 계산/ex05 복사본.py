#초를 입력받아서 시, 분, 초로 변경하는 프로그램

time = int(input("초를 입력하시오"))
second = int(time % 60)
minute = int((time / 60) % 60)
hour = (time / 60 ) // 60

print(hour," ",minute," ",second)