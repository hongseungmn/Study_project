from TV import *

if __name__ =="__main__":
    tv1 = TV()
    tv2 = TV()
    
    #인스턴스의 필드와 메서드를 tv1 인스턴스명(참조변수)를 조작을 하고 있다.
    tv1.color = "검정색"
    tv1.power(False,"tv1")
    tv1.channelUp(9)
    tv1.volumeUp(25)
    tv1.__str__()