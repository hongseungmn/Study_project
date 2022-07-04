import grade

def main():
    scoreList = grade.readList()
    scoreList.sort()
    grade.show_score(scoreList)

if __name__ =="__main__":
    main()