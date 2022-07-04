#반복문으로 문자열 관련 처리하기 실습
fruit = "apple"
#fruit 문자열 변수에 값을 하나씩 문자 형태로 가져와서 출력하는 코드
for letter in fruit:
    print(letter,end=" ")
    
    
print("")
print("-----------------------------------")
#사용자로부터 문자열(영문)을 입력받아서 모음을 전부 없애는 코드

s = input("문자열을 입력하세요(영문만): ")
#영문자의 모음의 문자열
vowels = "aeiouAEIOU"
result = ""

for letter in s:
    #하나씩 반복하는 문자가 모음 문자열에 존재하지 않는 경우
    if letter not in vowels:
        result += letter

print("자음만 출력",result)
        
print("")        
print("-----------------------------------")


#문자열을 입력받아서 자음과 모음의 개수를 집계하는 코드

original = input("문자열을 입력하시오(영문) : ")

word = original.lower() # 대문자로 바꾸고 싶다면 upper() 사용
vowels = 0
consonants = 0

#문자열의 길이가 0을 초과하고, 알파벳이라면 '...'참
if len(original) > 0 and original.isalpha():
    for ch in word:
        if ch in "aieou":
            vowels += 1
        else:
            consonants += 1
            
print("모음의 개수 :{0:}, 자음의 개수 :{1:}".format(vowels,consonants))


print("")        
print("-----------------------------------")
#사용자로부터 문자열을 입력받아서 알파벳 문자의 개수,숫자의 개수,스페이스 개수를 출력하는 코드

statements = input("문자열을 입력하세요(영문자,숫자,공백):")
alpha_cnt = 0
digit_cnt = 0
space_cnt = 0

for ch in statements:
    if ch.isalpha():
        alpha_cnt +=1
    elif ch.isdigit():
        digit_cnt +=1
    elif ch.isspace():
        space_cnt +=1
    else:
        print("해당하는 문자는 잘못 입력하셨습니다")
        
print("알파벳 개수:{0:} 숫자 개수:{1:}  공백문자 개수:{2:}".format(alpha_cnt,digit_cnt,space_cnt))
    
    
print("")        
print("-----------------------------------")
#사용자로부터 전화번호를 입력받을 때 "-"를 제거하는 코드

phone_number = input("전화번호를 입력하시오")
new_phone =""



for ch in phone_number:
    if ch !="-":
         new_phone += ch

if len(new_phone) < 11 or len(new_phone) >12:
    print("전화번호를 잘못 입력하셨습니다.")

else:
    print("정리한 전화번호:",new_phone)
