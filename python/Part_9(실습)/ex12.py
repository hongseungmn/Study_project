#클래스의 상속 : 조상(부모, 슈퍼) 클래스의 멤버(필드, 메서드, 생성자 제외) 
#들을 그대로 자손(자식, 서브)클래스가 물려받아 새로운 클래스를 만드는 것이다.
#이렇게 상속이 이루어지면 직접적인 관계가 이루어진다.
#조상 클래스의 멤버가 추가, 삭제, 수정에 따라서 자손클래스가 영향을 받는다.
#역으로 자손클래스의 멤버가 추가, 삭제, 수정이 되면 조상 클래스에 영향을 끼치지 않는다.
#자손 클래스로 내려가면 갈수록 멤버의 갯수가 많아지고 반대로 조상클래스로 올라가면 멤버의 갯수가 적어진다.

#조상 클래스
class Car:
    #조상 클래스의 멤버는 3개이다.

    
    def __init__(self):
        self.speed=0
        self.door=0
    
    def upSpeed(self,speed):
        self.speed += speed
        print("현재 속도(조상클래스) : %d" %self.speed)
        print("문의 갯수(조상클래스) : %d" %self.door)
        
#자손 클래스
class Sedan(Car):
    #자손 클래스의 멤버는 4개가 된다.
    def __init__(self,speed,door):
        #조상클래스의 생성자를 호출하는 부분이다.
        Car.__init__(self)
        self.speed = speed
        self.door = door
    
    #자손클래스에서 추가한 메서드
    def downSpeed(self,speed):
        self.speed -= speed
        print("현재 속도(자손클래스) : %d" %self.speed)
        

if __name__=="__main__":
    car = Car()
    #car.downSpeed(100) 호출 불가 #Car클래스의 메서드 호출
    print("car 주소 : ",id(car))
    sedan = Sedan(100,4)
    print("sedan 주소 : ",id(sedan))
    sedan.upSpeed(150)
    sedan.downSpeed(30)