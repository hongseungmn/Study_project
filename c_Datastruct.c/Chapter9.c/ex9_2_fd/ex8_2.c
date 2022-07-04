#include<stdio.h>
#include<stdlib.h>
#include"adjList.h"

void createGraph(graphType* g)
{
    int v;
    g->n=0;
    for(v=0;v<MAX_VERTEX;v++)
        g->adjList_H[v] =NULL;
}

void insertVertex(graphType* g,int v)
{
    if(((g->n)+1) > MAX_VERTEX)
    {
        printf("\n 그래프 정점의 개수를 초과하였습니다!");
        return;
    }
    g->n++;
}

void insertEdge(graphType* g,int u,int v)
{
    graphNode* node;

    if(u>=g->n || v>=g->n)
    {
        printf("\n 그래프에 없는 정점입니다!");
        return;
    }

    node = (graphNode*)malloc(sizeof(graphNode));
    node->vertex = v;
    node->link = g->adjList_H[u];
    g->adjList_H[u] = node;
}

void print_adjList(graphType* g)
{
    int i;
    graphNode* p;
    for(i=0;i<g->n;i++)
    {
        printf("\n\t\t정점 %c의 인접 리스트",i+65);
        p = g->adjList_H[i];
        while(p)
        {
            printf("-> %c", p->vertex + 65);
            p = p->link;
        }
    }
}

int main(void)
{
    int i;
    graphType* G1 = (graphType*)malloc(sizeof(graphType));

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

    printf("\n G1의 인접 리스트");
    print_adjList(G1);
}