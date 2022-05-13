'''
-------------------------------------------------------
Math 140 - module 0 project 4
-------------------------------------------------------
author:   Shayla Sexton <sesexton@aggies.ncat.edu>        
          Myla Simmons  <mrsimmons@aggies.ncat.edu>  
          Lexi Jones  <acjones11@aggies.ncat.edu>                           
-------------------------------------------------------
Description:

https://en.wikipedia.org/wiki/Twin_prime    
https://en.wikipedia.org/wiki/Factorial_prime
    
-------------------------------------------------------
'''

# Do not change the following code. It is used to provide
# a list of prime numbers for you to use in the project

import sympy as sy
maxN = 50000
primes = list(sy.sieve.primerange(2,maxN+1))


#------------------------------------------------------
#------------------------------------------------------

# Part a)
# variable name: na
# Define an integer between 4 and max_N

na = 26

# Part b)
# variable name: factors_na
# Write a for loop to build a list of of the factors of na 
# note: include 1 and na in the list

# example: na = 6, factors_na = [1,2,3,6]


factors_na = []
for i in range(1,na+1,1):
  if (na%i == 0):
    factors_na.append(i)

#------------------------------------------------------
#------------------------------------------------------

# Part c)
# variable name: nb
# Define an integer between 4 and maxN

nb = 4598

# Part d)
# variable name: prime_factors_nb
# Write a for loop to build a list of of the prime factors of nb 
# note: nb is in the list if it is prime
# note: make use of the list primes above

# example: nb = 6, prime_factors_nb = [2,3]
# example: nb = 5, prime_factors_nb = [5]

prime_factors_nb = []

factors_nb = []
for i in range(1,nb+1,1):
  if (nb%i == 0):
    factors_nb.append(i)
    
for i in factors_nb:
    if i in primes:
        prime_factors_nb.append(i)


#------------------------------------------------------
#------------------------------------------------------

# Part e)
# variable name: twin_primes
# Write a for loop to build a list of of the twin primes below maxN 
# hint: make use of the list primes above

# example: twin_primes = [3,5,7,11,13,...]

twin_primes = []

for i in primes:
    plus = i+2
    sub = i-2
    if plus in primes and i not in twin_primes:
        twin_primes.append(i)
    if plus in primes and plus not in twin_primes:
        twin_primes.append(plus)

    if sub in primes and sub not in twin_primes:
        twin_primes.append(sub)
    if sub in primes and i not in twin_primes:
        twin_primes.append(i)

    
#------------------------------------------------------
#------------------------------------------------------

# Part f)
# variable name: factorials
# Write a for loop to build a list of factorials below maxN
# note: do not use while loops or break statements
# hint: use a binary search


factorials = [1] # factorials for 1

for i in range(2,maxN,1):
    fac = i*factorials[-1] 
    if (fac < maxN):
        factorials.append(fac)
    else:
        add_by = maxN - i
        i += add_by
        
        
# Part g)
# variable name: factorial_primes
# Write a for loop to build a list of of the factorial primes below maxN
# hint: make use of the list primes above
# hint: make use of the list factorials above

# example: factorial_primes = [2,3,5,...]

factorial_primes = []
for i in factorials:
        if i+1 in primes and i < maxN:
            factorial_primes.append(i+1)
        if i-1 in primes and i < maxN:
            factorial_primes.append(i-1)
            

            






