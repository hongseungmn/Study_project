# CSV 파일은 split() 메소드로 파싱(분리)을 할 수 있다.
# CSV 파일을 읽는 프로그램을 작성해보자

def main():
    f_name = open(file="파일의 경로 작성",mode="r",encoding="UTF-8")
    #read() : 파일을 처음부터 끝까지 읽을 때 사용
    #readline() : 파일의 내용을 한 줄씩 읽어들일 때 사용
    #readlines() : 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소로 들어간다.
    for line in f_name.readlines():
        # 공백문자 제거
        line = line.strip()
        print(line)
        print(type(line))
        
        # 한 라인을 단어 토큰으로 나누어 출력
        words = line.split(",")
        for word in words:
            print("    ",word)

    f_name.close()
    
if __name__ =="__main__":
    main()