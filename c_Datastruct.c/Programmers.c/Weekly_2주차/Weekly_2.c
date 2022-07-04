#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

#define _USE_MATH_DEFINES
#include<math.h>

int dfs_board[50][50] = { 0 };
int dfs_table[50][50] = { 0 };
int dot_game_board[101][101] = { 0 };
int dot_table[101][101] = { 0 };

int board_order = 0;
int table_order = 0;
int indices = 0;
int count = 0;


char game_board_polyomino[6][625][50] = { 0 }, table_polyomino[6][625][50] = { 0 };
int polyomino[50] = { 0 };