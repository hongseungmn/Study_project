#자손 클래스인 Marine을 정의함
from Unit import *

class Marine(Unit):
    mode = ""
    
    #조상클래스의 추상메서들 오버라이딩
    def move(self,x,y):
        self.x = x
        self.y = y
        print("마린의 위치 : ",self.x, ",", self.y,"로 이동함")
        
        
    #Marine 자신만의 고유 기능을 추가
    def stimPack(self):
        self.mode = "공격모드 : 스팀팩 장전!"
        print(self.mode)