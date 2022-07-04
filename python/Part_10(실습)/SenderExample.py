#ContentSender, KakaoSender, SmsSender 클래스의 실행 파일이다

from KakaoSender import *
from SmsSender import *

if __name__ =="__main__":
    cs1 = KakaoSender("카카오톡","이재훈","100만원 갚아라")
    cs1.sendMsg("빚쟁이 이재훈")
    print("-------------------------")
    cs2 = SmsSender("SMS 문자","홍성민","고마워 ")
    cs2.sendMsg("앞으로도 잘 부탁")