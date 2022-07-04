#include<stdio.h>
#include "stackS.h"

int top = -1;

//스택이 공백인지 확인
int isStackEmpty(void)
{
    if(top ==-1) return 1;
    else return 0;
}

//스택이 포화 상태인지 확인 
int isStackFull(void)
{
    if(top == STACK_SIZE-1) return 1;
    else return 0;
}

//스택의 top에 원소를 삽입하는 연산
void push(element item)
{
    if(isStackFull())
    {
        printf("\n\n stack is FULL!\n");
        return;
    }
    else stack[++top] = item;
}

element pop(void)
{
    if(isStackEmpty())
    {
        printf("\n\n stack is EMPTY!\n");
        return 0;
    }
    else return stack[top--];
}

element peek(void)
{
    if(isStackEmpty())
    {
        printf("\n\n stack is EMPTY!\n");
        return 0;
    }
    else return stack[top];
}

void printStack(void)
{
    int i;
    printf("\n STACK [ ");
    for(int i=0;i<=top; i++)
    {
        printf("%d ",stack[i]);
    }
    printf("] ");
}
