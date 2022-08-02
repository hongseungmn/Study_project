# 스레드 실습
# 프로세스 : 하나의 응용어플리케이션 프로그램이 메모리에 로딩이 되어 CPU에 실행된 상태
# 스레드 : 하나의 프로세스 내에서 작업 단하물, 1~ n개까지 만들 수 있다. 
# 하나의 코어는 하나의 스레드를 도맡아서 처리한다. 코어가 많을수록 PC의 처리능력이 좋다
# 메인 스레드 : 파이썬 인터프리터가 제일 먼저 시작하는 부분을 메인 스레드라고 칭한다
# 메인 스레드는 여러 개의 서브(작업)스레드를 만들어서 실행시킬 수가 있다.
# 특정 스레드가 또 다른 스레드를 실행하는 것도 가능하다
# 서브 스레드를 만들어서 병렬로 코드를 실행시킬 수 있다 이것이 바로 스레드를 이용한 멀티 태스킹을 의미하는 것이다
# 메인스레드가 작업스레드보다 뭔지 종료가 되더라도, 작업 스레드가 계속실행중이라면 프로세스는 종료되지 않는다


from concurrent.futures import thread
import threading
import time

# 스레드 클래스 정의
# 스레드가 되기 위해서는 threadimg.Thread 클래스를 상속을 반드시 받아야 한다
class Worker(threading.Thread):
    #생성자
    def __init__(self, name):
        super().__init__()  # 조상클래스 생성자 호출
        self.name = name
        
    # CPU 스케줄러에 따라서 특정 스레드가 먼저 시작하였다 하더라도, CPU스케쥴러에 따라서 종료하는 스레드의 형ㅗ도 가능ㅎㄴ다
    def run(self):
        print("작업 스레드 시작 : ",threading.currentThread().getName())
        time.sleep(3)
        print("작업스레드 종료 : ",threading.currentThread().g다tName())
        
if __name__ == "__main__":
    print("메인스레드 시작")
    # 5개의 스레드가 생성되고 시작된다
    for i in range(5):
        name = "스레드->{}".format(i)
        t = Worker(name)    #   작업스레드 생성
        t.start()           # 작업 스레드에 구혀노디어 있는 w