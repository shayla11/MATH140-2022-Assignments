'''
-------------------------------------------------------
Math 140 - module 1 project 2
-------------------------------------------------------
author:   Shayla Sexton  <sesexton@aggies.ncat.edu>        
          Letitia Stinson-Miller  <stinsonl@aggies.ncat.edu>  
-------------------------------------------------------
Description: Data analysis

Data set name : BuddyMove
number of attributes : 7
number of instances : 249

Attribute 1 : (str) Unique user id
Attribute 2 : (int) Number of reviews on stadiums, sports complex, etc.
Attribute 3 : (int) Number of reviews on religous institutions
Attribute 4 : (int) Number of reviews on beach, lake, river, etc 
Attribute 5 : (int) Number of reviews on theaters, exhibitions, etc
Attribute 6 : (int) Number of reviews on malls, shopping places, etc.
Attribute 7 : (int) Number of reviews on parks, picnic spots, etc.

-------------------------------------------------------
'''

# Part a) 
# - go to
#   https://archive.ics.uci.edu/ml/datasets/BuddyMove+Data+Set
#   and read the description of the data set
# - download the data file (.csv file)
# - fill in the missing values in the description of the data set above


# Part b) ----------------------------------------------------
# import NumPy and Pandas

import numpy as np
import pandas as pd

# Part c) ----------------------------------------------------
# variable name : buddy_move_array
# - load the data using Pandas and extract the array of data from the
#   dataframe
# - note : set the correct value for header when loading
#        hint: the first line contains column labels
# - note : you may load from either the website or the downloaded file

url = 'buddymove_holidayiq.csv'
df = pd.read_csv(url,delimiter=',',header=0)
buddy_move_array = df.values 



# Part d) ----------------------------------------------------
# variable name : relig_max_ind
# - use the argmax() function to find the row index corresponding to the
#   user who had the maximum number of reviews of religious institutions 

relig_max_ind = np.argmax(buddy_move_array[:,2])

# Part e) ----------------------------------------------------
# variable name : relig_max_user
# - find the user id of the
#   user who had the maximum number of reviews of religious institutions 

relig_max_user = buddy_move_array[relig_max_ind,0]

# Part f) ----------------------------------------------------
# variable name : relig_max
# - find the maximum number of reviews of religious institutions 

relig_max = buddy_move_array[relig_max_ind, 2]

# Part g) ----------------------------------------------------
# variable name : relig_sum
# - find the total number of reviews of religious institutions 
#   for all users


relig_sum = np.sum(buddy_move_array[:,2])

# Part h) ----------------------------------------------------
# variable name : relig_mean
# - find the average number of reviews of religious institutions 

relig_mean = np.mean(buddy_move_array[:,2])

# Part i) ----------------------------------------------------
# variable name : relig_var
# - find the variance of reviews of religious institutions 


relig_var = np.var(buddy_move_array[:,2])


# Part j) ----------------------------------------------------
# variable name : mean_max
# - which column has the highest mean (excluding the first)

mean_max = np.argmax(np.mean(buddy_move_array[:,[1,2,3,4,5,6]], axis=0))+1


# Part j) ----------------------------------------------------
# variable name : var_min
# - which column has the smallest variance (excluding the first)

var_min = np.argmin(np.var(buddy_move_array[:,[1,2,3,4,5,6]], axis=0))+1


# Part k) ----------------------------------------------------
# variable name : mean_rev_34
# - find the average number of reviews provided by user 34


mean_rev_34 = np.mean(buddy_move_array[35,2:7])


# Part l) ----------------------------------------------------
# variable name : parks_over_100_mask
# - create a mask for the users who provided more than 100 reviews 
#   of parks, picnic spots, etc


parks_over_100_mask = buddy_move_array[:,6] > 100

# Part m) ----------------------------------------------------
# variable name : parks_over_100
# - extract an array of the users who provided more than 100 reviews 
#   of parks, picnic spots, etc


parks_over_100 = buddy_move_array[parks_over_100_mask,:]

# Part n) ----------------------------------------------------
# variable name : parks_over_100_count
# - how many users provided more than 100 reviews 
#   of parks, picnic spots, etc

parks_over_100_count = np.shape(parks_over_100)[0]











