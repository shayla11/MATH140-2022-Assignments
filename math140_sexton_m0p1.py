'''
-------------------------------------------------------
Math 140 - module 0 project 1
-------------------------------------------------------
author:   Shayla    <sesexton@aggies.ncat.edu>        
          Shandler  <samason1@aggies.ncat.edu>  
          Sean      <smwalters@aggies.ncat.edu>                              
-------------------------------------------------------
Description:
    Working with lists
    Fill in code where prompted
    
    You will need to download the files 
    -m0p1List1.npy
    -m0p1List2.npy
    from blackboard and place them in the same folder
    as your script.
    The first few lines of code are used to import 
    two lists from these files.
-------------------------------------------------------
'''

# import the numpy package
import numpy as np 

# import data
List1 = list(np.load('m0p1List1.npy'))
List2 = list(np.load('m0p1List2.npy'))



# Part a) ----------------------------------------------------
# variable name : len_L1
# compute the number of items in List1


len_L1 = len(List1)



# Part b) ----------------------------------------------------
# variable name : len_L2
# compute the number of items in List2

len_L2 = len(List2)


# Part c) ----------------------------------------------------
# variable name : max_L2
# Find the maximum value of List2

max_L2 = max(List2)

# Part d) ----------------------------------------------------
# variable name : min_L2
# Find the minimum value of List2

min_L2 = min(List2)


# Part e) ----------------------------------------------------
# Sort List2 in ascending order
# Store the item of index 101 in the variable L2sort_asc_101

new_L2_sort = sorted(List2)
L2sort_asc_101 = new_L2_sort[101]


# Part f) ----------------------------------------------------
# Sort List2 in descending order
# Store the item of index 101 in the variable L2sort_dec_101

new_L2_sort = sorted(List2, reverse=True)
L2sort_dec_101 = new_L2_sort[101]


# Part g) ----------------------------------------------------
# variable name : sum_L2
# find the sum of the numbers in List2

sum_L2 = sum(List2)


# Part h) ----------------------------------------------------
# variable name : L1_n101
# Find the item of index -101 in List1

L1_n101 = List2[-101]

# Part i) ----------------------------------------------------
# variable name : sum_slice_1
# Find the sum of the numbers in List2 with even index
# note: this refers to the unsorted List2 

sum_slice_1 = sum(List2[0:453:2])

# Part j) ----------------------------------------------------
# variable name : sum_slice_2
# Find the sum of the numbers in List2 with odd index


sum_slice_2 = sum(List2[1:453:2])


# Part k) ----------------------------------------------------
# variable name : count_a
# count the number of times the letter 'a' appears in List1

count_a = List1.count('a')

# Part l) ----------------------------------------------------
# step 1 : slice List1 to extract the items of index 15,18,21,24,...,45,48,51
#          store the result as list_l1
# step 2 : append the letter 'b' (as a string) to the end of list_l1
# step 3 : count the number of occurences of 'b' in list_l1
#          store the result as count_b

list_l1 = List1[15:52:3]
list_l1.append('b')
count_b = list_l1.count('b')
