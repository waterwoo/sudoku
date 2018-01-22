#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:13:37 2018

@author: waterwoo
"""

'''
create arr
'''
arr = [[0 for i in range(9)] for j in range(9)]
#for i in range(9):
#    for j in range(9):
#        arr[i][j] = i * 9 + j + 1

'''
accept input
'''

with open('sudoku.txt', 'r') as f:
    arry = f.readline()
for i in range(81):
    arr[int(i/9)][i%9] = int(arry[i])
    
def deal_num(x):
    candidate = [[0 for m in range(9)] for n in range(9)]
    for i in range(9):
        for j in range(9):
            if x[i][j] == 0:
                a = '123456789'
                for k in range(9):
                    for l in range(9):
                        if k == i:
                            aa = str(x[k][l])
                            a = a.replace(aa, '')
                        elif l == j:
                            aa = str(x[k][l])
                            a = a.replace(aa,'')
                        elif int(i/3) == int(k/3) and int(j/3) == int(l/3):
                            aa = str(x[k][l])
                            a = a.replace(aa, '')
                candidate[i][j] = a
                
                                
    return candidate
    


def num_select(x, y):
    for i in range(9):
        for j in range(9):
            if x[i][j] in ('1','2','3','4','5','6','7','8','9'):
                y[i][j] = int(x[i][j])



def column(x, y):
    '''
    column
    '''
    for i in range(9):
        stri_list = ''
        for j in range(9):
            if x[i][j] != 0:
                stri_list += str(x[i][j])
        for k in range(9):
            if stri_list.count(str(k+1)) == 1:
                for l in range(9):
                    if str(x[i][l]).find(str(k+1)) != -1:
                        y[i][l] = k+1

                
def row(x, y):
    '''
    column
    '''
    for j in range(9):
        stri_list = ''
        for i in range(9):
            if x[i][j] != 0:
                stri_list += str(x[i][j])
        for k in range(9):
            if stri_list.count(str(k+1)) == 1:
                for l in range(9):
                    if str(x[l][j]).find(str(k+1)) != -1:
                        y[l][j] = k+1        
                        
def nine_palace(x, y):
    for k in range(3):
        for l in range(3):
            stri_list = ''
            for i in range(9):
                for j in range(9):
                    if k == int(i/3) and l == int(j/3):
                        stri_list += str(x[i][j])
            for m in range(9):
                if stri_list.count(str(m+1)) == 1:
                    for row in range(9):
                        for col in range(9):
                            if k == int(row/3) and l == int(col/3):
                                if str(x[row][col]).find(str(m+1)) != -1:
                                    y[row][col] = m+1

'''
nine_palace's function maybe repeated by col and row
'''
                                
    

co = 0
while True:
    num_select(deal_num(arr), arr)
    column(deal_num(arr), arr)
    row(deal_num(arr), arr)
    nine_palace(deal_num(arr), arr)
    co += 1
    if co > 20:
        break

#delt_num_list = deal_num(arr)
#num_select(delt_num_list, arr)
#delt_num_list = deal_num(arr)
#column(delt_num_list, arr)
#delt_num_list = deal_num(arr)
#row(delt_num_list, arr)
