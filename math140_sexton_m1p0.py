'''
-------------------------------------------------------
Math 140 - module 1 project 0
-------------------------------------------------------
author:   Shayla Sexton  <sesexton@aggies.ncat.edu>        
          Your Name  <yourEmail@ncat.edu>  
          Your Name  <yourEmail@ncat.edu>                           
-------------------------------------------------------
Description:
    1D arrays
-------------------------------------------------------
'''

# Part a) ----------------------------------------------------
# import the numpy package 

import numpy as np 


# Part b) ----------------------------------------------------
# variable name : arr1
# data type : int
# create an array of the integers 10,20,30,...,1000

arr1 = np.arange(10,1001,10,dtype=int) 

# Part c) ----------------------------------------------------
# variable name : arr1_even
# Slice arr1 to extract the items with even index


arr1_even = arr1[0:np.shape(arr1)[0]:2]


# Part d) ----------------------------------------------------
# variable name : arr1_list_slice
# Slice arr1 using a list to extract the items with indices 10,5,2,0,11

ls = [10,5,2,0,11]
arr1_list_slice = arr1[ls]

# Part e) ----------------------------------------------------
# variable name : arr2
# data type : float
# create an array of zeros of length 200

arr2 = np.zeros((200,), dtype=float)

# Part f) ----------------------------------------------------
# variable name : arr3
# data type : float
# create an array of ones of length 200

arr3 = np.ones((200,), dtype=float)

# Part g) ----------------------------------------------------
# variable name : arr4
# data type : float
# create an array of the integers 0,1,2,...,199

arr4 = np.arange(0,200,1, dtype=float)

# Part h) ----------------------------------------------------
# variable name : arr_sum
# add arr3 and arr4 componentwise

arr_sum = arr3 + arr4

# Part i) ----------------------------------------------------
# file name : arr_sum.npy
# save arr_sum as an .npy file

np.save('arr_sum.npy',arr_sum)


# Part j) ----------------------------------------------------
# file name : arr_sum.txt
# save arr_sum as an .txt file

np.savetxt('arr_sum.txt',arr_sum) 


# Part k) ----------------------------------------------------
# variable name : arr_obj
# data type : object
# create an array from the list [2,'hello',5.0]

arr_obj = np.array([2, 'hello', 5.0], dtype=object)

# Part l) ----------------------------------------------------
# file name : arr_obj.npy
# save arr_obj as an .npy file

np.save('arr_obj.npy',arr_obj)


# Part m) ----------------------------------------------------
# variable name : arr_obj_load
# load arr_obj.npy from the previously saved file

arr_obj_load = np.load('arr_obj.npy',allow_pickle=True)


# Part n) ----------------------------------------------------
# variable name : compare
# variable type : Boolean
# check if arr_sum and arr2 have the same entries

compare = np.array_equal(arr_sum, arr2)

# Part o) ----------------------------------------------------
# variable name : arr_sum_len
# variable type : int
# find the length of arr_sum
# hint: do not forget to unpack the tuple

arr_sum_len = np.shape(arr_sum)[0]







