#include<stdio.h>
#include<stdlib.h>
#include"node2.h"

treeNode* searchBST(treeNode* root,element x);
treeNode* insertBSTNode(treeNode* p,element x);
void deleteBSTNode(treeNode* root,element key);

treeNode* searchBST(treeNode* root,element x)
{
    treeNode* p;
    int count =0;
    p =root;
    while(p != NULL)
    {
        count++;
        if(x<p->key)p=p->left;
        else if(x==p->key)
        {
            printf("%3d번째에 탐색 성공",count);
            return p;
        }
        else p = p->right;
    }
    count++;
    printf("%3d번째에 탐색 실패! 찾는 키가 없습니다!",count);
    return p;
}

void deleteBSTNode(treeNode* root,element key)
{
    treeNode *parent, *p, *succ, *succ_parent;
    treeNode *child;

    parent =NULL;
    p =root;
    while((p !=NULL) && (p->key !=key))
    {
        parent = p;
        if(key < p->key)p = p->left;
        else p =p->right;
    }
    
    if(p == NULL)
    {
        printf("\n 찾는 키가 이진트리에 없습니다!");
        return;
    }

    if((p->left == NULL) &&(p->right==NULL))
    {
        if(parent != NULL)
        {
            if(parent->left ==p) parent->left =NULL;
            else parent->right = NULL;
        }
        else root = NULL;
    }

    else if((p->left == NULL) || (p->right == NULL))
    {
        if(p->left != NULL) child = p->left;
        else child = p->right;

        if(parent != NULL)
        {
            if(parent->left == p) parent->left = child;
            else parent->right =child;
        }
        else root = child;
    }

    else
    {
        succ_parent = p;
        succ = p->left;
        while(succ->right != NULL)
        {
            succ_parent = succ;
            succ = succ->right;
        }
        if(succ_parent->left ==succ)succ_parent->left = succ->left;
        else succ_parent->right = succ->left;
        p->key =succ->key;
        p = succ;
    }

    free(p);
}