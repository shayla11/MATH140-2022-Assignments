#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:19:49 2022

@author: shayla
"""

import numpy as np

arr = np.load('q4_array.npy',allow_pickle=True)

a = 10
b = 7

a = 3
if a > 4:
    b = 7
elif a>0:
    b = 5
    
ar_size = np.shape(arr)
ar_max = np.max(arr)
ar_min = np.min(arr)
    
    
