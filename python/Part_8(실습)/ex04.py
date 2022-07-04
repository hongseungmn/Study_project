#딕셔너리의 동등성 비교
#동등성은 논리적 동등이라는 것을 의미한다. 논리적 동등이란 주소는 다르나
# 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점이다.

#일반적인 딕셔너리의 동등성 비교
dic1 = {"가":1,"나":2,"다":3}
dic2 = {"가":1,"다":2,"나":3}
print(id(dic1))
print(id(dic2))
print(dic1 == dic2)
#주소는 틀리지만 값은 동일하므로 true를 리턴한다.

from collections import OrderedDict 
ordered_dic1 = OrderedDict({"가":1,"나":2,"다":3}) 
ordered_dic2 =OrderedDict({"가":1,"다":2,"나":3})
print(id(ordered_dic1))
print(id(ordered_dic2))
print(ordered_dic1==ordered_dic2)
#OrderedDict는 순서까지 비교하므로 False가 출력된다.
