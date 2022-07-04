
import math


class Circle:
    
    __radius =0
    
    def __init__(self,radius):
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return math.pi * self.__radius * self.__radius
    
    def getRound(self):
        return math.pi * 2 * self.__radius
    
    
    def __str__(self):
        print("원의 반지름 : ",self.getRadius())
        print("원의 넓이 : ",self.getArea())
        print("원의 둘레 : ",self.getRound())