#StopIteration 예외 발생시키기 실습
list1 = [10,20,30]

# iter() 내장함수로 리스트를 이터레이터로 쓸 수 있도록 설정
list1_iter = iter(list1)
#list1 = list1.__iter__()

# __next__()이용하여 값을 가져오도록 한다
print("결과값 : ",list1_iter.__next__())
print("결과값 : ",list1_iter.__next__())
print("결과값 : ",list1_iter.__next__())
print("결과값 : ",list1_iter.__next__())
