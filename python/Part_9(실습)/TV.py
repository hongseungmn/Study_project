#클래스 TV를 설계하는 코드
class TV:
    #필드를 선언
    color = ""      #색상
    power = False   #전원
    channel = 0     #채널
    volume = 0      #볼륨
    
    #TV의 전원을 키거나 끄는 멤버 메서드
    def power(self,power,tv):
        self.power = not power
        if self.power == True:
            print("%s TV의 전원이 켜졌습니다." % tv)
        else :
            print("%s TV의 전원이 껴졌습니다." % tv)
        
    #TV의 채널을 올리는 기능을 하는 멤버 메서드
    def channelUp(self,channel):
        if channel <0:
            print("채널은 음수일 수 없습니다.")
            return
        if self.power ==False:
            print("TV의 전원부터 켜주세요.")
            return
        self.channel += channel
    #TV의 채널을 내리는 기능을 하는 멤버 메서드
    def channelDown(self,channel):
        if channel <0:
            print("채널은 음수일 수 없습니다.")
            return
        if self.power ==False:
            print("TV의 전원부터 켜주세요.")
            return
        self.channel -= channel
        
    #
    def volumeUp(self,volume):
        if volume <0:
            print("음량은 음수일 수 없습니다.")
            return
        if self.power ==False:
            print("TV의 전원부터 켜주세요.")
            return
        self.volume += volume
        
    def volumeDown(self,volume):
        if volume <0:
            print("음량은 음수일 수 없습니다.")
            return
        if self.power ==False:
            print("TV의 전원부터 켜주세요.")
            return
        self.volume -= volume
        
    #__str__() 인스턴스의 멤버변수들의 값을 찍어보는 용도로 사용된다.
    def __str__(self):
        print("TV의 색상 : %s" % self.color)
        print("TV의 채널 : %d" % self.channel)
        print("TV의 볼륨 : %s" % self.volume)