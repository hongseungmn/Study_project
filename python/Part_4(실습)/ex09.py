#매개변수는 함수의 선언부에 존재하며 함수가 호출될 때 비로소 메모리에 할당이 된다. 함수가 종료되면 매개변수도 소멸이 된다.
#매개변수도 지역변수의 일종이다.

def list_test(my_list):
    #매개변수로 넘어온 my_list에 새로운 리스트를 할당
    my_list = [1,2,3,4]
    print(my_list)
    return

my_list = [100,200,300,400]
list_test(my_list)
print(my_list)
