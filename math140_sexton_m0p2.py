'''
-------------------------------------------------------
Math 140 - module 0 project 2
-------------------------------------------------------
author:   Shayla Sexton   <sesexton@aggies.ncat.edu>        
          Payton Sanford  <pcsanford@aggies.ncat.edu>  
          Sydni  Sharpe   <sasharpe@aggies.ncat.edu>                           
-------------------------------------------------------
Description:
    Working with conditionals
    
    
Background: https://en.wikipedia.org/wiki/System_time
For Unix systems, time starts January 1, 1970, 00:00:00 (UTC),
and time is counted in seconds since this epoch.
This project deals with conversion between our normal
date-time (month, day, hour, second) and an analog of
system time.

Note :
    In some calculations, it may be helpful to introduce
    additional variables. However, make sure that the
    names do not overlap with those requested
    in the project
    
-------------------------------------------------------
'''


# Part a) ----------------------------------------------------
# variable name : day1
# define an integer between 1 and 365


day1 = 116


# Part b) ----------------------------------------------------
# variable name : month_list1
# define a list of length 12, where each item is the number of
# days in the month for a common year: jan,feb,mar,...

month_list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Part c) ----------------------------------------------------
# variable name : month_day1
# Goal: day1 specifies a day in a common year. Find the month 
#       and day of the month corresponding to day1. Store the
#       month as a string and the day as an integer in a 
#       list of length 2
# - use a conditional statement 
# - hint : there should be at least 10 elif statements in your 
#          conditional statement
# - hint : use the sum() function on a slice of month_list1
#          as conditions in your conditional
    
month_day1 = []
if day1 - sum(month_list1[0:1]) < 0 : #jan
    month_day1 = ["jan", day1]
elif day1 - sum(month_list1[0:2]) < 0 : #feb
    month_day1 = ["feb", day1 - sum(month_list1[0:1])]
elif day1 - sum(month_list1[0:3]) < 0: #mar
    month_day1 = ["mar", day1 - sum(month_list1[0:2])]
elif day1 - sum(month_list1[0:4]) < 0: #apr
    month_day1 = ["apr", day1 - sum(month_list1[0:3])]
elif day1 - sum(month_list1[0:5]) < 0: #may
    month_day1 = ["may", day1 - sum(month_list1[0:4])]                                  
elif day1 - sum(month_list1[0:6]) < 0: #jun
    month_day1 = ["jun", day1 - sum(month_list1[0:5])]  
elif day1 - sum(month_list1[0:7]) < 0: #jul
    month_day1 = ["jul", day1 - sum(month_list1[0:6])]      
elif day1 - sum(month_list1[0:8]) < 0: #aug
    month_day1 = ["aug", day1 - sum(month_list1[0:7])]  
elif day1 - sum(month_list1[0:9]) < 0: #sep
    month_day1 = ["sep", day1 - sum(month_list1[0:8])]   
elif day1 - sum(month_list1[0:10]) < 0: #oct
    month_day1 = ["oct", day1 - sum(month_list1[0:9])]  
elif day1 - sum(month_list1[0:11]) < 0: #nov
    month_day1 = ["nov", day1 - sum(month_list1[0:10])] 
else: #dec
    month_day1 = ["dec", day1 - sum(month_list1[0:11])] 


#-------------------------------------------------------------
#-------------------------------------------------------------


# Part d) ----------------------------------------------------
# variable name : month_day2
# define a list of length 2. The first item is a month as a 
# string. The second item is an integer between 1 and the 
# number of days in that month.

month_day2 = ["may", 24]


# Part e) ----------------------------------------------------
# variable name : day2
# use a conditional statement to find the day of the year 
# corresponding to month_day2
# - hint : there should be at least 10 elif statements in your 
#          conditional statement
# - hint : use the sum() function on a slice of month_list1
#          as part of your computation

day2 = 0
if month_day2[0] == "jan":
    day2 = month_day2[1]
elif month_day2[0] == "feb":
    day2 = sum(month_list1[0:1]) + month_day2[1]
elif month_day2[0] == "mar":
    day2 = sum(month_list1[0:2]) + month_day2[1]
elif month_day2[0] == "apr":
    day2 = sum(month_list1[0:3]) + month_day2[1]
elif month_day2[0] == "may":
    day2 = sum(month_list1[0:4]) + month_day2[1]
elif month_day2[0] == "jun":
    day2 = sum(month_list1[0:5]) + month_day2[1]
elif month_day2[0] == "jul":
    day2 = sum(month_list1[0:6]) + month_day2[1]
elif month_day2[0] == "aug":
    day2 = sum(month_list1[0:7]) + month_day2[1]
elif month_day2[0] == "sep":
    day2 = sum(month_list1[0:8]) + month_day2[1]
elif month_day2[0] == "oct":
    day2 = sum(month_list1[0:9]) + month_day2[1]
elif month_day2[0] == "nov":
    day2 = sum(month_list1[0:10]) + month_day2[1]
else:
    day2 = sum(month_list1[0:11]) + month_day2[1]


#-------------------------------------------------------------
#-------------------------------------------------------------


# Part f) ----------------------------------------------------
# variable name : sec3
# define an integer between 0 and 31535999
# - for this problem sec3 is the time in seconds after midnight
#   at the start of a new common year

sec3 =  14578900


# Part g) ----------------------------------------------------
# variable name : day3
# find the number of days that have passed (0-364) 
# after sec3 seconds
# hint : use // for integer division 
# hint : you may want to save the remainder as well for later parts


day3 = sec3//86400
day3_r = sec3%86400 # seconds left over


# Part h) ----------------------------------------------------
# variable name : hour3
# regarding sec3, find the number of hours that have passed (0-23) 
# after day3 days have passed 


hour3 = day3_r//3600 
hour3_r = day3_r%3600 #seconds left over


# Part i) ----------------------------------------------------
# variable name : minute3
# regarding sec3, find the number of minutes that have passed (0-59) 
# after day3 days have passed and hour3 hours have passed 


minute3 = hour3_r//60
minute3_r = hour3_r%60 #seconds left over


# Part j) ----------------------------------------------------
# variable name : second3
# regarding sec3, find the number of seconds that have passed (0-59) 
# after day3 days have passed and hour3 hours have passed and
# minute3 minutes have passed 


second3 = hour3_r%60


# Part l) ----------------------------------------------------
# variable name : date_time
# combine the results from parts g)-j) in a list
# [days,hours,minutes,seconds]


date_time = [day3, hour3, minute3, second3]


# Part m) (bonus) --------------------------------------------
# variable name : date_time_bonus
# find the month (string) correspoonding to date_time using a 
# conditional and define a new list
# [month,day of the month,hour,minute, second]
# hint : if day3 is 0, the day of the month is 1 
# note : use a 24 hour day: 1pm would be 13 hours



if day3 - sum(month_list1[0:1]) < 0 : #jan
    date_time_bonus = ["jan", day3 , hour3, minute3, second3]
elif day3 - sum(month_list1[0:2]) < 0 : #feb
    date_time_bonus = ["feb", day3 - sum(month_list1[0:1]), hour3, minute3, second3]
elif day3 - sum(month_list1[0:3]) < 0: #mar
    date_time_bonus = ["mar", day3 - sum(month_list1[0:2]), hour3, minute3, second3]
elif day3 - sum(month_list1[0:4]) < 0: #apr
    date_time_bonus = ["apr", day3 - sum(month_list1[0:3]), hour3, minute3, second3]
elif day3 - sum(month_list1[0:5]) < 0: #may
    date_time_bonus = ["may", day3 - sum(month_list1[0:4]), hour3, minute3, second3]                                  
elif day3 - sum(month_list1[0:6]) < 0: #jun
    date_time_bonus = ["jun", day3 - sum(month_list1[0:5]), hour3, minute3, second3]  
elif day3 - sum(month_list1[0:7]) < 0: #jul
    date_time_bonus = ["jul", day3 - sum(month_list1[0:6]), hour3, minute3, second3]      
elif day3 - sum(month_list1[0:8]) < 0: #aug
    date_time_bonus = ["aug", day3 - sum(month_list1[0:7]), hour3, minute3, second3]  
elif day3 - sum(month_list1[0:9]) < 0: #sep
    date_time_bonus = ["sep", day3 - sum(month_list1[0:8]), hour3, minute3, second3]   
elif day3 - sum(month_list1[0:10]) < 0: #oct
    date_time_bonus = ["oct", day3 - sum(month_list1[0:9]), hour3, minute3, second3]  
elif day3 - sum(month_list1[0:11]) < 0: #nov
    date_time_bonus = ["nov", day3 - sum(month_list1[0:10]), hour3, minute3, second3] 
else: #dec
    date_time_bonus = ["dec", day3 - sum(month_list1[0:11]), hour3, minute3, second3] 


