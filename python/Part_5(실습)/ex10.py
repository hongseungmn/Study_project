#일반적인 리스트 연산들 실습
#최소값 최대값을 구하는 알고리

#아래 코드는 내장 함수를 이용하여 구하는 코드이다.
num = [1,5,-9,100]
print(min(num))
print(max(num))

prices = [1000,3000,500,10000,20000,700]
#먼저 prices[]에 있는 0번째 인덱스 값을 변수에 저장한다.
lowPrice = prices[0]
#이후, 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice 변수에 재저장
for i in range(1,len(prices)): # 부등호만 바꾸면 가장 큰 값을 출력할 수 있다.
    if prices[i] < lowPrice:
        lowPrice = prices[i]
        
print(lowPrice)

#문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
words = ["dog","cat","horse","lion","tiger","elephant"]
#문자열 리스트에서 min()는 제일 첫 글자가 아스키코드 중에서 가장 작은 단어를 반환해준다.
print(min(words))

shortest_word = words[0]
list_words = []
for i in range(len(words)):
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            list_words.clear()
            list_words.append(words[i])
        
        