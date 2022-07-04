#pragma once 
typedef char element;

typedef struct treeNode 
{
    element key;
    struct treeNode* left;
    struct treeNode* right;
}treeNode;

void displayInorder(treeNode* root);

#include<stdio.h>

void displayInorder(treeNode* root)
{
    if(root)
    {
        displayInorder(root->left);
        printf("%c_",root->key);
        displayInorder(root->right);
    }
}