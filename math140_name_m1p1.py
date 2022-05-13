'''
-------------------------------------------------------
Math 140 - module 1 project 1
-------------------------------------------------------
author:   Shayla Sexton sesexton@aggies.ncat.edu      
          Your Name  <yourEmail@ncat.edu>  
          Your Name  <yourEmail@ncat.edu>                           
-------------------------------------------------------
Description:
    
    Note: use NumPy functions rather than builtin functions
          to receive full credit. For example, use np.shape()
          rather than len(). These are important for 
          higher dimensional arrays which will appear in
          upcoming projects.
-------------------------------------------------------
'''

# Part a) ----------------------------------------------------
# import NumPy

import numpy as np

# Part b) ----------------------------------------------------
# variable name : arr1
# load the object array in m1p1arr1.npy

arr1 = np.load('m1p1arr1.npy',allow_pickle=True)

# Part c) ----------------------------------------------------
# variable name : arr2
# load the integer array in m1p1arr2.npy

arr2 = np.load('m1p1arr2.npy',allow_pickle=True)


# Part d) ----------------------------------------------------
# variable name : arr3
# load the integer array in m1p1arr3.npy

arr3 = np.load('m1p1arr3.npy',allow_pickle=True)


# Part e) ----------------------------------------------------
# variable name : len_1
# data type : int
# compute the number of items in arr1


len_1 = np.shape(arr1)

# Part f) ----------------------------------------------------
# variable name : len_2
# data type : int
# compute the number of items in arr2

len_2 = np.shape(arr2)


# Part g) ----------------------------------------------------
# variable name : max_2
# Find the maximum value of arr2

max_2 = np.max(arr2)

# Part h) ----------------------------------------------------
# variable name : min_2
# Find the minimum value of arr2

min_2 = np.min(arr2)


# Part i) ----------------------------------------------------
# variable name : mask_g10
# create a mask for the items in arr2 that are greater than 10

mask_g10 = arr2 > 10 #items greater than 10

# Part j) ----------------------------------------------------
# variable name : arr2_g10
# use mask_g10 to slice arr2 to extract the numbers greater than 10

arr2_g10 = arr2[mask_g10]

# Part k) ----------------------------------------------------
# variable name : min_ind_3
# find the index of the minimum value in arr3

min_ind_3 = np.argmin(arr3)


# Part l) ----------------------------------------------------
# variable name : max_ind_3
# find the index of the maximum value in arr3

max_ind_3 = np.argmax(arr3)


# Part m) ----------------------------------------------------
# variable name : sum_1
# Find the sum of the numbers in arr2_g10

sum_1 = np.sum(arr2_g10)

# Part n) ----------------------------------------------------
# variable name : avg_3
# Find the average of the numbers in arr3


avg_3 = np.mean(arr3)


# Part o) ----------------------------------------------------
# variable name : var_3
# find the variance of the numbers in arr3


var_3 = np.var(arr3)



# Part p) ----------------------------------------------------
# variable name : prod_1
# Find the product of the numbers less than 25 in arr3

mask_p1 = arr3 < 25
arr3less25 = arr3[mask_p1]
prod_1 = np.prod(arr3less25) #theres a 0 in the data, resulting in 0

