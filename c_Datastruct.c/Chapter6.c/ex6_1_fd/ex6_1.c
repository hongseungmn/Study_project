
#include<stdio.h>
#include<stdlib.h>
#include"queueS.h"

QueueType* createQueue(void)
{
    QueueType* Q;
    Q= (QueueType*)malloc(sizeof(QueueType));
    Q->front = -1;
    Q->rear = -1;
    return Q;
}

int isQueueEmpty(QueueType* Q)
{
    if(Q->front == Q->rear)
    {
        printf("Queue is empty!\n\t");
        return 1;
    }
    else return 0;
}

int isQueueFull(QueueType* Q)
{
    if(Q->rear == Q_SIZE-1)
    {
        printf("Queue is full!\n\t");
        return 1;
    }
    else return 0;
}

void enQueue(QueueType* Q,element item)
{
    if(isQueueFull(Q))return;
    else{
        Q->rear++;
        Q->queue[Q->rear] =item;
    }
}

element deQueue(QueueType* Q)
{
    if(isQueueEmpty(Q))return 0;
    else
    {
        Q->front++;
        return (Q->queue[Q->front]);
    }
}

element peekQ(QueueType* Q)
{
    if(isQueueEmpty(Q)) return 0;
    else return (Q->queue[Q->front+1]);
}

void printQ(QueueType* Q)
{
    printf("Queue: [");
    for(int i = Q->front+1;i<=Q->rear;i++)
        printf("%3c",Q->queue[i]);
    printf(" ]");
}
int main(void)
{
    QueueType* Q1 = createQueue();
    element data;
    
    printf("\n ***** 순차 큐 연산 *****\n");
    printf("\n 삽입 A>> "); enQueue(Q1,'A');printQ(Q1);
    printf("\n 삽입 B>> "); enQueue(Q1,'B');printQ(Q1);
    printf("\n 삽입 C>> "); enQueue(Q1,'C');printQ(Q1);
    data = peekQ(Q1); printf(" peek item : %c \n",data);
    printf("\n 삭제  >> "); data = deQueue(Q1);printQ(Q1);
    printf("\t 삭제 데이터: %c",data);
    printf("\n 삭제  >> "); data = deQueue(Q1);printQ(Q1);
    printf("\t 삭제 데이터: %c",data); 
    printf("\n 삭제  >> "); data = deQueue(Q1);printQ(Q1);
    printf("\t 삭제 데이터: %c",data);
    
    printf("\n 삽입 D>> "); enQueue(Q1,'D');printQ(Q1);
    printf("\n 삽입 E>> "); enQueue(Q1,'E');printQ(Q1);

    
    return 0;
}