'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 1, intro to Python   

- data types
     string - sequence of characters
     int - integer numbers
     float - floating point numbers
- built in functions
     print() - displays items in the console
     len() - compute the length of a string (as well as other data types)
- operations
     number computations +,-,*,/,**
     integer specific computations  //,%
     basic string slicing
     define muli-line comment
     define single line comment
     assign a number to a variable
     assign a string to a variable

'''

#------------------------------------------------------------

'''
multi-line comments begin and end with 3 apostrophes
'''

# this is a single line comment 

#------------------------------------------------------------

print('hello world!')

print(3,'hello')


#------------------------------------------------------------

string1 = 'Hello World'

print(string1)

n1 = 34

print(n1)

#------------------------------------------------------------

# string - is a sequence of characters 
#        - defined using apostrophes

# variable_name = value 

s2 = '83294024832kjlkdfjsdf  fgld k;fkfldslfk##%%^%*^*&^*'


#------------------------------------------------------------

# integer arithmetic

i1 = 5

i2 = 10

i3 = i1*i2 # muliplication

i31 = 5*10

i4 = i1+i2 # addition

integer_subtraction_1 = i1-i2  # subtraction

i5 = i2//i1

i6 = 5//2 # quotient for 5/2

i7 = 5%2 # remainder for 5/2

i8 = 5/2 # gives floating point result

i9 = 2**5 # exponentiation

#------------------------------------------------------------

# floating point arithmetic

f1 = 3.14

f2 = 2.0

f3 = f1/f2 # division

f4 = f1**f2


#------------------------------------------------------------

# slicing
# - indexing starts at 0 
# - variable_name[starting index : endinging index + 1 ] 

s3 = '0123456789'

s4 = s3[0:5]

print(s4)

s5 = s3[2:7]

s6 = 'hello world'

s7 = s6[0:5 ] # extract hello

print(s7)

s8 = s6[6:11] # extract world

print(s8)

#-----------------------------------------------------------

# functions

print('hello world')

l1 = len(s6)

print(l1)

#-----------------------------------------------------------

# data structure : lists
# bounded by square brackets
# items separated by commas

l1 = [2,3,4,5,1] # list of numberss

l2 = ['hello', 'world'] # list of strings

l3 = [34,15,'hello']



#------------------------------------------------------------

# functions on lists

length_l1 = len(l1)

length_l2 = len(l2)

sum_l1 = sum(l1)

min_l1 = min(l1)










