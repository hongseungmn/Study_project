#Phone 클래스의 자손 클래스인 DmbPhone 클래스 정의

from pyexpat import model
from Phone import *


class DmbPhone(Phone):
    #멤버의 개수가 12개이다
    #생성자
    def __init__(self,model,color,channel):
        #조상클래스 생성자 호출 2가지 방법
        #자손 클래스 생성자 구현부의 첫 줄에 적는 것을 권장한다.
        #super().__init__()
        Phone.__init__(self)
        self.model=model
        self.color = color
        self.channel = channel
        
    #메서드 추가
    def turnOnDmb(self):
        print("채널 : ",self.channel, "번 DMB 방송수신을 시작합니다")
    def turnOffDmb(self):
        print("DMB 방송수신을 멈춥니다")
    def changeChannelDmb(self,channel):
        self.channel = channel
        print("채널 : ",self.channel,"번으로 바꿉니다")
        

#Phone 클래스와 DmbPhone 클래스를 이용하여 메인코드 작성 부분
if __name__ == "__main__":
    # 자손 클래스의 인스턴스 생성
    dmbPhone = DmbPhone("Python Phone","Black",10)
    
    #조상 클래스에게 상속받은 필드
    print("모델 : ",dmbPhone.model)
    print("색생 : ",dmbPhone.color)
    
    #자손 클래스 필드
    print("채널 : ",dmbPhone.channel)
    
    dmbPhone.powerOn()
    dmbPhone.bell()
    dmbPhone.sendVoice("여보세요")
    dmbPhone.receiveVoice("안녕하세요 반갑습니다")
    
    dmbPhone.hangUp()
    
    #자손 클래스에서 만든 DMB 기능
    
    dmbPhone.turnOnDmb()
    dmbPhone.changeChannelDmb(15)
    dmbPhone.turnOffDmb()
    