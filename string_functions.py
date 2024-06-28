s1='Welcome to'

s1[0:len(s1):]
# 'Welcome to'

print(s1.upper())
# WELCOME TO

print(s1.lower())
# welcome to

print(s1.capitalize())
# first character is converted to uppercase 
# Welcome to

print(s1.title())
# first character of every word is capitalized
# Welcome To

print(s1.isupper())
# only if all letters are capitalized , it will return true
# False


print(s1.islower())
# only if all letters are small , it will return true
# False

print(s1.isspace())
# checks if all characters are spaces
# False

print(s1.isalpha())
# checks if all the characters are alphabets
# Note: This will come as False because of the whitespace.
# False

print(s1.isalnum())
# checks if all characters are alphabets or numbers
# note : its coming false because of space
# False

x="12"
print(x.isdigit())
# True 
# Note: isdigit() is a function of string and checks if the string contain only digits or not 

# Note : startswith and endswith function also return the boolean values only 
print(s1.startswith('w'))
# False

print(s1.startswith('W'))
# True 

print(s1.endswith('e'))
# False
# since the string is ending with o

print(s1.endswith('E'))
# False
# since the string is ending with O

# *********IMP ************

# 1) count()
# finding the number of e's present inside the string s1
print(s1.count('e'))
# 2

# finding the number of substrings present inside a particular string 
s1.count('Welcome')
# can be used for substrings to

# 2) find()
s1.find('e')
# returns the first index

# 3) Welcome
s1.find('e',5)
# second parameter is the starting index
# 6
# parameters in find(a,b,c)
# a --> string to be found 
# b --> starting index
# c --> ending index

s1.find('e',2,2)
# -1

# if the element is present it will return the index of element
# if the element is not present it will return -1

# Note : There is no difference between the index() and the find()

# both the things are exactly the same just replace find with index and 
# nothing else.

s1.replace("to","in")
# replace first parameter with second parameter

s2="welcome to to to to Deloitte"
s2.replace("to","in",3)
#replaces the word for three times


# Split and Join
# Split will return lists
# Default split criteria is space

s2.split('welcome')
# ['', ' to to to to Deloitte']

s2.split("to")
# # Split and Join
# Split will return lists
# Default split criteria is space

s2.split('welcome')




