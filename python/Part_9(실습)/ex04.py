#Monitor 클래스를 이용한 실습

from Monitor import *

if __name__ =="__main__":
    monitor1 = Monitor("Apple",13,15000000,"silver")
    monitor1.__str__()
    
    print("===========================================")
    monitor1.setCompany("SamSung")
    monitor1.setInch("19")
    monitor1.setPrice("10000000")
    monitor1.setColor("Black")
    monitor1.__str__()