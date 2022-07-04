
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


long long solution(int price, int money, int count) {
    long long answer = -1;
    long long all_price=0;
    for (int i = 1;i<=count;i++){
        all_price += price *i;
    }
    if (all_price>money){
        answer = all_price - money;
    }
    else{
        answer = 0;
    }
    return answer;
}

int main(void)
{
    int price = 3;
    int money = 20;
    int count = 4;

    long long answer = solution(price,money,count);

    printf("%lld\n",answer);

}
