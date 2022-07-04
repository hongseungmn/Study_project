# 함수를 이용하여 딕셔너리를 초기화 하는 코드를 실습하기

from collections import defaultdict
# 일반 딕셔너리 함수를 이용하여 초기화 방법
def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열의 값을 하나가 키가 되고 그 키의 기본값을 0으로 설정함
        if letter not in counter:
            counter[letter] = 0
    return counter

#setdefault() 메서드를 이용한 초기화 방법
def countLetters_setdefault(word):
    counter = {}
    for letter in word:
        #위의 countLetters() 보다 조건절은 사라졌으나 루프를 돌 때마다,
        #setdefault()를 계속 호출하므로 비효율적 코드다
        counter.setdefault(letter, 0)
        
    return counter 

#defaultdict 모듈을 직접 이용하는 방법
def countLetters_defaultdict(word):
    #이 함수에서는 defaultdict()만 한 번 호출이 일어난다.
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] +=1
    return counter


if __name__ =="__main__":
    dic = countLetters("가나다라마")
    print(dic.items())
    dic = countLetters_setdefault("가나다라마")
    print(dic.items())
    dic = countLetters_setdefault("가나다라마")
    print(dic.items())
