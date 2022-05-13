'''
-------------------------------------------------------
Math 140 - module 1 project 3
-------------------------------------------------------
author:   Shayla Sexton  sesexton@aggies.ncat.edu        
          Shandler Mason  samason1@aggies.ncat.edu  
-------------------------------------------------------
Description: Haar wavelets

- notes are provided on Blackboard  (m1p3.pdf)
- a numpy array is provided on Balckboard (m1p3.npy)

-------------------------------------------------------
'''

# Part a) 
# import numpy

import numpy as np

# Part b) 
# variable name : image
# - load the array m1p3.npy from Blackboard

image = np.load("m1p3.npy", allow_pickle=True)#20 by 30

# Part c) 
# variable names : rows, cols
# - compute the number of rows and columns in the array

rows = np.shape(image)[0]
cols = np.shape(image)[1]

# Part d) 
# variable names : typeI, typeII, typeIII, typeIV
# - initialize 4 arrays of zeros, with float data type
# - the size should depend on the size of image
# - refer to the notes for the exact size

typeI = np.zeros((rows//2,cols//2), dtype=float)
typeII = np.zeros((rows//2,cols//2), dtype=float)
typeIII = np.zeros((rows//2,cols//2), dtype=float)
typeIV = np.zeros((rows//2,cols//2), dtype=float)

# Part e) 
# Use nested for-loops to fill in the values of typeI as described
# in the notes

for i in range(0,rows//2):
    for j in range(0,cols//2):
        a = image[2*i, 2*j]
        b = image[2*i, 2*j+1]
        c = image[2*i+1, 2*j]
        d = image[2*i+1, 2*j+1]
        typeI[i,j] = (a+b+c+d)/2
        
# Part f) 
# Use nested for-loops to fill in the values of typeII as described
# in the notes

for i in range(0,rows//2):
    for j in range(0,cols//2):
        a = image[2*i, 2*j]
        b = image[2*i, 2*j+1]
        c = image[2*i+1, 2*j]
        d = image[2*i+1, 2*j+1]
        typeII[i,j] = (a+b-c-d)/2

# Part g) 
# Use nested for-loops to fill in the values of typeIII as described
# in the notes

for i in range(0,rows//2):
    for j in range(0,cols//2):
        a = image[2*i, 2*j]
        b = image[2*i, 2*j+1]
        c = image[2*i+1, 2*j]
        d = image[2*i+1, 2*j+1]
        typeIII[i,j] = (a-b+c-d)/2

# Part h) 
# Use nested for-loops to fill in the values of typeIV as described
# in the notes

for i in range(0,rows//2):
    for j in range(0,cols//2):
        a = image[2*i, 2*j]
        b = image[2*i, 2*j+1]
        c = image[2*i+1, 2*j]
        d = image[2*i+1, 2*j+1]
        typeIV[i,j] = (a-b-c+d)/2



#Extension
def m1p3function(array):
    
    typeI = np.zeros((rows//2,cols//2), dtype=float)
    typeII = np.zeros((rows//2,cols//2), dtype=float)
    typeIII = np.zeros((rows//2,cols//2), dtype=float)
    typeIV = np.zeros((rows//2,cols//2), dtype=float)
    
    for p in range(0,4): #Number of Types
        #locals()['type'+str(p)] = np.zeros((rows//2,cols//2), dtype=float)
        
        for i in range(0,rows//2):
            for j in range(0,cols//2):
                a = image[2*i, 2*j]
                b = image[2*i, 2*j+1]
                c = image[2*i+1, 2*j]
                d = image[2*i+1, 2*j+1]
                if (p == 0): #Based of each type, change the function
                    typeI[i,j] = (a+b+c+d)/2
                elif (p == 1):
                    typeII[i,j] = (a+b-c-d)/2
                elif (p == 2):
                    typeIII[i,j] = (a-b+c-d)/2
                elif (p == 3):
                    typeIV[i,j] = (a-b-c+d)/2
   
    return (typeI, typeII, typeIII, typeIV)

print(m1p3function(image))
    
    
    
    
    
    
    
    
    
    
    
    
    
    