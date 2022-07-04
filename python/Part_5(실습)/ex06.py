#리스트 복사하기
#얕은 복사(shallow copy) : 주소값을 공유하는 개념, 원본 리스트에 영향을 끼치는 복사 방법
#엄밀히 얘기하면 진정한 복사가 아니다.

scores = [10,20,30,40,50]
refer = scores #scores의 주소값을 refer 변수에게 복사
print("scores의 주소값 :",id(scores))
print("refer의 주소값 :".id(refer))
refer[0] =100
refer.append(-70)
refer.insert(1,-100)
print(id(scores))
print(id(refer))
print(scores)
print(refer)

#리스트 복사하기
#깊은 복사(deep copy) : 주소값을 공유하는 얕은 복사가 아니라 새로운 리스트 객체를
#생성해서 새로운 주소값이 할당이 되어 원본 리스트 객체에는 전형 영향을 끼치지 아니한다.

#첫 번째 방법 : list()메서드를 이용하는 방법
scores=[10,20,30,40,50]
refer = list(scores)
print(id(scores))
print(id(refer))
refer[0] = -100
refer.append(-500)
refer.insert(2,123)

print(id(scores))
print(id(refer))
print(scores)
print(refer)

#두 번째 방법 : copy() 모듈에 있는 deepcopy(),copy()를 이용하는 방법
import copy

scores_copy=[10,20,30,40,50]
refer_copy = copy.deepcopy(scores_copy) # copy()를 사용해도 된다.
print(id(scores))
print(id(refer))
refer_copy[0] = -100
refer_copy.append(-500)
refer_copy.insert(2,123)

print(id(scores_copy))
print(id(refer_copy))
print(scores_copy)
print(refer_copy)

#세 번째 방법 : [:]인덱스를 이용하여 깊은 복사를 하는 방법
scores_index=[10,20,30,40,50]
refer_index = scores_index[:]
print(id(scores_index))
print(id(refer_index))
refer_index[0] = -100
refer_index.append(-500)
refer_index.insert(2,123)

print(id(scores_index))
print(id(refer_index))
print(scores_index)
print(refer_index)

