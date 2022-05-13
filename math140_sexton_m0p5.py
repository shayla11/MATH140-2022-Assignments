'''
-------------------------------------------------------
Math 140 - module 0 project 5
-------------------------------------------------------
author:   Shayla Sexton sesexton@aggies.ncat.edu        
                         
-------------------------------------------------------
Description:

Writing functions
    
-------------------------------------------------------
'''


#------------------------------------------------------
#------------------------------------------------------

# Part a)
# create the following function
# function name: factors
# input: n (an integer greater than 1)
# output: a list of the factors of n (including 1 and n)



def factors(n):
    facts = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            facts.append(i)
    return facts
            
#print(factors(10))
    
    
#------------------------------------------------------
#------------------------------------------------------

# Part b)
# create the following function
# function name: isprime
# input: n (an integer greater than 1)
# output: a Boolean value (True if n is prime or 
#                           False if n is composite) 


def isprime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


#------------------------------------------------------
#------------------------------------------------------

# Part c)
# create the following function
# function name: month
# input: n (an integer between 1 and 365)
# output: the month (as a string) corresponding to the 
#          nth day of the year



def month(n):
    ml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if n - sum(ml[0:1]) < 0 : #jan
        return "January"
    elif n - sum(ml[0:2]) < 0 : #feb
        return "February"
    elif n - sum(ml[0:3]) < 0: #mar
        return "March"
    elif n - sum(ml[0:4]) < 0: #apr
        return "April"
    elif n - sum(ml[0:5]) < 0: #may
        return "May"                                 
    elif n - sum(ml[0:6]) < 0: #jun
        return "June"  
    elif n - sum(ml[0:7]) < 0: #jul
        return "July"     
    elif n - sum(ml[0:8]) < 0: #aug
        return "August"  
    elif n - sum(ml[0:9]) < 0: #sep
        return "September"  
    elif n - sum(ml[0:10]) < 0: #oct
        return "October" 
    elif n - sum(ml[0:11]) < 0: #nov
        return "November" 
    elif n - sum(ml[0:12]) < 0: #dec
        return "December"
    else:
        return "Index out of range"
    


#------------------------------------------------------
#------------------------------------------------------

# Part d)
# create the following function
# function name: fact
# input: n (an integer greater than 1)
# output: a list of the factorials  0!,1!,2!,3!,...,n!



def fact(n):
    f = [1]

    for i in range(1,n+1,1):
        fac = i*f[-1] 
        f.append(fac)
    return f



#------------------------------------------------------
#------------------------------------------------------
 
# Part e)
# create the following function
# function name: math140
# input: None
# output: your name (as a string)


def math140():
    return "Shayla Sexton"
