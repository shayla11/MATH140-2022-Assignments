#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:11:50 2022

Shayla Sexton sesexton@aggies.ncat.edu
Shandler Mason samason1@aggies.ncat.edu

"""

# import statement - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import numpy as np


# variables - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
current_pos = 0 #start on go square
max_spaces = 40 #total spaces on board
rolls = 10**6*5 #number of times to roll the dice
dice_sides = 4
#space_counts = np.zeros((max_spaces,), dtype=float)
#space_counts = {i:0 for i range(max_spaces)}
space_counts = [0 for i in range(max_spaces)]
doubles = 0; #numbers of consecutive doubles rolled

cc_card = 0 # current top card in community chest stack
# 0 - advanced to go
# 1 go to jail

ch_card = 0 # current top card in chance stack
# 0 - Advance to Go (0)
# 1 - Got to jail (10)
# 2 - Go to C1 (11)
# 3 - Go to E3 (24)
# 4 - Go to H2 (39)
# 5 - Go to R1 (5)
# 6 - Go to next R (railway company) Railways (5,15,25,35)
# 7 - Go to next R Railways (5,15,25,35)
# 8 - Go to next U (utility company) Utilities (12,28)
# 9 - Go back 3 squares

# game play - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for roll in range(rolls):
    
    space_counts[current_pos] +=1
    
    die1 = np.random.randint(1,dice_sides+1)
    die2 = np.random.randint(1,dice_sides+1)
    #check for roll for doubles
    
    if (die1 == die2):
        doubles +=1
    else:
        doubles = 0
    
    if doubles == 3:
        current_pos = 10 #jail is 10th spot
        doubles = 0
        continue #skips everything in the loop
    
    current_pos = (current_pos+die1+die2)%max_spaces
    #print(die1, die2, current_pos)
    
    #chance
    if current_pos in [7,22,36]: # the chance spaces
        if ch_card == 0:
            current_pos = 0 #advance to go
        elif ch_card == 1:
            current_pos = 10 #go to jail
        elif ch_card == 2:
            current_pos = 11 # go to C1
        elif ch_card == 3:
            current_pos = 24 # go to E3
        elif ch_card == 4:
            current_pos = 39 # go to H2
        elif ch_card == 5:
            current_pos = 5 # go to R1
        elif ch_card == 6 or ch_card == 7:
            if current_pos == 7:
                current_pos = 15 # second railroad
            elif current_pos == 22:
                current_pos = 35 # fourth raliraod
            elif current_pos == 36:
                current_pos = 5 # first railroad
        elif ch_card == 8: 
            if current_pos == 7:
                current_pos = 12 #electric company
            elif current_pos == 22:
                current_pos = 28 #water works
            elif current_pos == 36:
                current_pos = 12 #electric company
        elif ch_card == 9:
            current_pos = current_pos-3 #go back 3 spaces
        
        ch_card = (ch_card+1)%16 #puts the card at the bottom of the deck

            
    #community chest
    if current_pos in [2,17,33]: #the community chest spaces
        if cc_card == 0:
            current_pos = 0 #advance to go
        elif cc_card == 1:
            current_pos = 10 # go to jail
        cc_card = (cc_card+1)%16 #puts the card at the bottom of the deck
        
    if current_pos == 30:
        current_pos = 10
    



# analysis - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#print(space_counts)
percentages = [space_counts[i]/rolls*100 for i in range(max_spaces)]
percentages = [np.around(p,3) for p in percentages]
print(percentages)
print()


#sort by percentages
percentages_negative = [-p for p in percentages]
indices = np.argsort(percentages_negative)
print(indices)
print()

top_spot = str(indices[0]).zfill(2)
sec_spot = str(indices[1]).zfill(2)
thir_spot = str(indices[2]).zfill(2)
print(top_spot+sec_spot+thir_spot) # 4 sided die








