#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:29:17 2022

@author: shayla
"""
a = [2, 3, 4, 5, 4, 3, 6, 7, 9]

b = sorted(a) #increasing
c = sorted(a, reverse=True) #decresing

d = b[0:20:2]
e = b[0:3]
f = b[6:9]

g = c + d
h = len(g)

i = [1, 1, 1, 2, 2, 2, 6, 7, 8, 9]
j = min(i)
k = max(i)
l = sum(i)
m = i.index(6)
n = i.append(10)
o = i.count(1)