#include<stdio.h>
#include"stackL.h"
#include"evalPostfix.h"

int main()
{
    int result;
    char* express = "35*62/-";
    printf("후위 표기식 : %s ", express);

    result = evalPostfix(express);
    printf("\n\n 연산결과 => %d\n",result);

    getchar(); return 0;
}