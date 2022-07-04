#pragma once
#include<stdio.h>

typedef int element;

typedef struct treeNode
{
    element key;
    struct treeNode* left;
    struct treeNode* right;
}treeNode;

void displayInorder(treeNode* root);

void displayInorder(treeNode* root)
{
    if(root)
    {
        displayInorder(root->left);
        printf("%d_",root->key);
        displayInorder(root->right);
    }
}