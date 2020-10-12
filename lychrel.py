#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:57:28 2020
"""

import math
print('Write a number with 2 digits or more:')

p = input()
lp = len(p)
nn = ''
paly=False
c2 = 0
while not paly:
    for i in range(lp):
        nn = nn + str(p[lp-i-1])
        suma = str(int(nn)+int(p))
        ls = len(suma)
    
    c=0
    ls2 = math.floor(ls/2)
    
    for j in range(ls):
        z = int(suma[j])-int(suma[ls-j-1])
        if z == 0:
            c = c + 1

    c2 = c2 + 1
    print('\n'+str(c2)+':\t'+str(p)+'+'+str(nn)+'='+str(suma))
          
    if c == ls:
        paly=True
    p = suma
    lp = len(p)
    nn = ''


