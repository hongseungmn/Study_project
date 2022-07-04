#매개변수가 있는 생성자에 대한 실습
class Monitor :
    #필드 선언
    
    __company =""
    __inch = 0
    __price = 0
    __color = ""
    
    #파이썬에서는 1개 이상의 생성자를 만들 수 없다.
    #오버로딩 : 같은 메서드명으로 다른 일을 하게끔 만드는 작업
    #매개변수의 타입과 개수에 따라서 같은 이름의 메서드라도 다른 메서드가 호출이 되는 형태를 지칭한다.
    # def __init__(self):
    #     print("기본생성자 호출")
    
    
    def __init__(self,company,inch,price,color):
        #self.company는 멤버 변수를 칭하는 것이며, company는 외부에서 생성자를 호출할 때 
        #매개변수 값으로 들어오는 것을 의미한다.
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color
    
    def setCompany(self,company):
        self.__company = company
    def setInch(self,inch):
        self.__inch = inch
    def setPrice(self,price):
        self.__price = price
    def setColor(self,color):
        self.__color = color   
    
        
    def getCompany(self):
        return self.__company
    def getInch(self):
        return self.__inch
    def getPrice(self):
        return self.__price
    def getColor(self):
        return self.__color    
        
    
        
        
    def __str__(self):
        print("제조사 : ", self.getCompany())
        print("인치 : ", self.getInch())
        print("가격 : ", self.getPrice())
        print("색상 : ", self.getColor())
        
        
        