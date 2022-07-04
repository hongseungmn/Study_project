#OrededDict 모듈 이름 그대로 순서를 가지는 딕셔너리 객체이다.
#원래, 딕셔너리는 순서를 보장하지 않는 객체이다.

#일반적인 딕셔너리는 순서를 보장하지 않는다. 
#딕셔너리는 인덱스가 없기 때문이다.
#파이썬의 버전이 올락가면서 일반 딕셔너리가 입력된 순서대로
#정확하게 출력이 되고 있다.
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k,v in dic.items():
    print(k,v)
    
print("------------------------------------------")
#OrderedDict는 딕셔너리의 순서와 동등성 비교를 개선한 모듈이다.
from collections import OrderedDict

dic = OrderedDict()
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k,v in dic.items():
    print(k,v)
    
    
    
    
    
#일반 딕셔너리를 정렬알 하여 OrderedDict로 포장하기
#넘어오는 t의 값은 딕셔너리의 요소이다.
#하여 0인덱스는 키값이 될 것이다.
def sort_by_key(t):
    return t[0] # [0]은 key값을 기준으로 정렬을 하고, [1]은 value값을 기준으로 정렬을 하게 된다.

dic1 = {}
dic1["z"] = 100 # z:100
dic1["a"] = 200
dic1["e"] = 300
dic1["d"] = 400

#일반 딕셔너리의 내용을 sorted()를 이용하여 정렬을 하면 키를 기준으로
#정렬된 리스트가 리턴된다. OderedDict()로 포장(wrapping)을 하고 있다.
#기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리의 형태로 관리를 할 수 있다.
for k,v in OrderedDict(sorted(dic1.items(),key=sort_by_key)).items():
    print(k,v)

print(sorted(dic1.items(),key=sort_by_key))
