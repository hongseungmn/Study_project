#include<stdio.h>
void SelectionSort(int a[],int size);

void SelectionSort(int a[],int size)
{
    int i,j,t,min,temp;

    for(i=0;i<size-1;i++)
    {
        min=i;
        for(j=i+1;j<size;j++)
        {
            if(a[j]<a[min]) min=j;
        }
        temp=a[i];
        a[i] = a[min];
        a[min]=temp;
        printf("\n%d단계 : ",i+1);
        for(t=0;t<size;t++)printf("%3d ",a[t]);
    }
}

int main(void)
{
    int i,list[8] = {69,10,30,2,16,8,31,22};
    int size = sizeof(list)/sizeof(list[0]);
    printf("\n 정렬할 원소 : ");
    for(i=0;i<size;i++)printf("%3d ",list[i]);
    printf("\n<<<<<<<<<<<<<<<<< 선택 정렬 수행 >>>>>>>>>>>>>>>>>>>");
    SelectionSort(list,size);
    getchar();return 0;
}