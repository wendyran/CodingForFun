# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:46:40 2015

@author: ranwei
"""
def LDN(N):
    div3 = {}
    div5 = {}
    
    for i in range(N + 1):
        if i % 3 == 0:
            div3[i] = N - i
        if i % 5 == 0:
            div5[i] = N - i
    
    for k in sorted(div5.keys()): 
        if div3.has_key(N-k):
            sum = ''
            for j in range(k, N):
                sum += '5'  
            for j in range(k):
                sum += '3'  
            
            return int(sum)
    
    return -1

n = int(raw_input())
for _ in range(n):
    N = int(raw_input())
    res = LDN(N)
    print res