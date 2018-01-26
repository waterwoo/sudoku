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
    candidate = [['0' for m in range(9)] for n in range(9)]
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
    '''
    nine_palace's function maybe repeated by col and row
    '''
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

def x_wing_row(x):
    
    
    stri_list = ['' for i in range(9)]
    for i in range(9):
        for j in range(9):
            if x[i][j] != 0:
                stri_list[i] += str(x[i][j])
    for num in range(9):
        a = [[0 for i in range(2)] for j in range(9)]
        b = 0
        for row in range(9):
            if str(stri_list[row]).count(str(num+1)) == 2:
                #print(row)
                c = 0
                for k in range(9):
                    if str(x[row][k]).find(str(num+1)) != -1:
                        a[row][c] = k
                        c += 1
                b += 1
        if b > 1:
                for n in range(9):
                    for m in range(9):
                        if a[n] == a[m] and n != m and a[n] != [0,0]:
                            
                            for l in range(9):
                                if l != n and l != m:                                    
                                    x[l][a[n][0]] = x[l][a[n][0]].replace(str(num+1), '')                                    
                                    x[l][a[n][1]] = x[l][a[n][1]].replace(str(num+1), '')                                    
    return x
    

def x_wing_col(x):
    stri_list = ['' for i in range(9)]
    for j in range(9):
        for i in range(9):
            if x[i][j] != 0:
                stri_list[j] += str(x[i][j])
    for num in range(9):
        a = [[0 for i in range(2)] for j in range(9)]
        b = 0
        for col in range(9):
            if str(stri_list[col]).count(str(num+1)) == 2:
                #print(row)
                c = 0
                for k in range(9):
                    if str(x[k][col]).find(str(num+1)) != -1:
                        a[col][c] = k
                        c += 1
                b += 1
        if b > 1:
                for n in range(9):
                    for m in range(9):
                        if a[n] == a[m] and n != m and a[n] != [0,0]:
                            
                            for l in range(9):
                                if l != n and l != m:                                    
                                    x[a[n][0]][l] = x[a[n][0]][l].replace(str(num+1), '')                                    
                                    x[a[n][1]][l] = x[a[n][1]][l].replace(str(num+1), '')                                    
    return x
        
co = 0
while True:
    numm = x_wing_row(x_wing_col(deal_num(arr)))
    num_select(numm, arr)
    column(numm, arr)
    row(numm, arr)
    nine_palace(numm, arr)
    
    co += 1
    if co > 50:
        
        break

