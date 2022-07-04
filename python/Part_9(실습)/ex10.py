# 1.지역 변수 : 함수 안에서 선언되는 변수
# 2.전역 변수 : 함수 외부에서 선언되는 변수, 프로그램 종료시 같이 소멸
# 3.인스턴스 변수 : 클래스 안에 선언된 변수, 앞에 self.을 붙여준다

class Bag:
    def __init__(self):
        self.data = []
    def add(self,x):
        self.data.append(x)
    def add2(self,x):
        #클래스 내에서 자신의 메소드를 호출하기 위해서도 self.을 붙여 주도록 한다
        self.add(x)
        self.add(x)
    def __str__(self):
        print("리스트의 값 : ",self.data)
        
        
        
        
# None 참조값 : 변수가 아무것도 가리키고 있지 않다면 None으로 초기화를 해주는 것이 권장 사항이다.
# 모든 변수는 초기화를 해주는 것이 좋다.
#None(C언어,자바에서는 null) 은 아무것도 참조하지 않고 있다는 특별한 값

class TV:
    # power = False
    # channel = 32
    # volume = 3
    def __init__(self,power,channel,volume):
        self.power = power
        self.channel = channel
        self.volume = volume
        
    def powerTV(self):
        self.power = not self.power
        
    def __str__(self):
        print(self.power)
        print(self.channel)
        print(self.volume)

if __name__ == "__main__":
    bag = Bag()
    bag.add(10)
    bag.__str__()
    bag.add2("서울")
    bag.__str__()
    
    tv = None
    # 결과가 None이 나오는 것이 당연하다. 인스턴스를 생성하지 않았으므로  
    #print(tv) 
    #AttributeError: 'NoneType' object has no attribute
    #TV가 없으므로 power 메서드를 호출할 수 없다.
    #tv.powerTV()
    tv = TV(True,10,25)
    tv.__str__()
    print("--------------------------------")
    tv.powerTV()
