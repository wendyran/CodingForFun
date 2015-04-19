# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:47:56 2015

@author: ranwei
"""
#==============================================================================
# Song of Pi
# https://www.hackerrank.com/challenges/song-of-pi
#==============================================================================
def PiSong(s):
    l = len(s)
    Pi = 31415926535897932384626433833
    lenPi = len(str(Pi))
    
    word = 1
    count = 0
    for i in range(l):
        if s[i] == ' ':
            if count == Pi/(10**(lenPi-word)):            
                count = 0
                Pi = Pi%(10**(lenPi-word))
                word += 1
            else:
                return "It's not a pi song."
        else:
            count += 1
            
    if word == 1:
        if count != 3:
          return "It's not a pi song."
          
    return "It's a pi song."

n = int(raw_input())
for k in range(n):
    s = raw_input()
    res = PiSong(s)
    print res