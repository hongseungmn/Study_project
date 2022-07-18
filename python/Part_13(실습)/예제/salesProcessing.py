# sales.txt 파일을 읽어서 총 매출과 평균 일매출을 파일로 내보내는 프로그램

# 사용자로부터 입력 파일 이름, 출력 파일 이름을 입력 받는다.
infilename = input("입력 파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

# 입출력을 하기 위해서 파일을 연다.
infile = open(infilename,"r")
outfile = open(outfilename,"w")

# 합계와 횟수를 위한 변수를 정의한다.
sum = 0
count = 0

#입력파일에서 한 줄을 읽어서 합계를 계산하고 평균을 구하기 위해서 count 변수값을 1씩 증가시키고 있다.
line = infile.readline()
while line != "":
    sales_num = int(line)
    sum += sales_num
    count += 1
    line = infile.readline().rstrip()
    

outfile.write("총 매출 = " + str(sum) + "\n")
outfile.write("평균 일매출 = " + str(sum/count))

infile.close()
outfile.close()
