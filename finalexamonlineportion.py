#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:06:25 2022

@author: shayla
"""

import numpy as np
import pandas as pd

url = 'krkopt.data'
df = pd.read_csv(url,delimiter=',',header=None)
array = df.values 

"""
column 0  White King file (column)
column 1 White King rank (row)
column 2 White Rook file
column 3 White Rook rank
column 4 Black King file
column 5 Black King rank
column 6 optimal depth-of-win for White in 0 to 16 moves, otherwise drawn {draw, zero, one, two, ..., sixteen}.
"""

#question 2
whitekingfile_a = np.sum(array[:,0]=="a")
blackkingrank_4 = np.sum(array[:,5]==4)
resultindraw = np.sum(array[:,6]=="draw")
optimalwin_12 = np.sum(array[:,6]=="twelve")

#question 3
draw_mask = array[array[:,6]=="draw"]
whiterook_5 = np.sum(draw_mask[:,3]==5)
whiterook_7 = np.sum(draw_mask[:,3]==7)

winonemove_mask = array[array[:,6]=="one"]
whiterook5_onewin = np.sum(winonemove_mask[:,3]==5)

#question 4
winone_avgwhiteking = np.mean(winonemove_mask[:,1])
winone_varwhiteking = np.var(winonemove_mask[:,1])
winone_avgblackking = np.mean(winonemove_mask[:,5])

#question 5
samefile = array[:,(0,2,4,6)]
possiblewin = []

for row in samefile:
    if row[0] == row[1] and row[0] == row[2]:
        possiblewin.append(row[3])
        
        
        








