#include<stdio.h>
#include<stdlib.h>
#include"traversalBT.h"
treeNode* makeRootNode(element data,treeNode* leftNode,treeNode* rightNode)
{
    treeNode* root = (treeNode*)malloc(sizeof(treeNode));
    root->data = data;
    root->left = leftNode;
    root->right = rightNode;
    return root;
}

//전위 순회
void preorder(treeNode* root)
{
    if(root)
    {
        printf("%c",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

//중위 순회
void inorder(treeNode* root)
{
    if(root)
    {
        inorder(root->left);
        printf("%c",root->data);
        inorder(root->right);
    }
}

//후위순회
void postorder(treeNode* root)
{
    if(root)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%c",root->data);
    }
}
