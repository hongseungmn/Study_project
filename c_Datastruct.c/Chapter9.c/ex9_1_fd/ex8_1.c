#include<stdio.h>
#include<stdlib.h>
#include"adjMatrix.h"

void createGraph(graphType* g)
{
    int i,j;
    g->n = 0;
    for(i=0;i<MAX_VERTEX;i++)
    {
        for(j=0;j<MAX_VERTEX;j++)
        {
            g->adjMatrix[i][j] = 0;
        }
    }
}

void insertVertex(graphType* g,int v)
{
    if(((g->n) +1) > MAX_VERTEX)
    {
        printf("\n 그래프의 정점의 개수를 초과하였습니다!");
        return;
    }
    g->n++;
}

void insertEdge(graphType* g,int u,int v)
{
    if(u >=g->n || v>=g->n)
    {
        printf("\n그래프에 없는 정점입니다!");
        return;
    }
    g->adjMatrix[u][v] = 1;
}

void print_adjMatrix(graphType* g)
{
    int i,j;
    for(i=0;i<(g->n);i++)
    {
        printf("\n\t\t");
        for(j=0;j<(g->n);j++)
        {
            printf("%2d",g->adjMatrix[i][j]);
        }
    }
}

int main(void)
{
    int i;
    graphType* G1 = (graphType*)malloc(sizeof(graphType));
    graphType* G2 = (graphType*)malloc(sizeof(graphType));
    graphType* G3 = (graphType*)malloc(sizeof(graphType));
    graphType* G4 = (graphType*)malloc(sizeof(graphType));


    createGraph(G1);
    for(i=0;i<4;i++)
        insertVertex(G1,i);
    insertEdge(G1,0,3);
    insertEdge(G1,0,1);
    insertEdge(G1,1,3);
    insertEdge(G1,1,2);
    insertEdge(G1,1,0);
    insertEdge(G1,2,3);
    insertEdge(G1,2,1);
    insertEdge(G1,3,2);
    insertEdge(G1,3,1);
    insertEdge(G1,3,0);

    


    printf("\n G1의 인접 행렬");
    print_adjMatrix(G1);
}