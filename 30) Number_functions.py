# -----------------------abs ----------------------------------

abs(-1)
# 1

abs(-1.1)
# 1.1

# --------------------round-------------------------------------

round(10.9)
# 11

round(10.4)
# 10

# at .5 , mistakes can happen . So be careful there.

# 0.5 rounds off to closest even integers
round(9.5)
# 10

round(8.5)
# 8

round(10.5)
# 10

# by default the value of second parameter is 0
round(10.3421,1)
# 10.3

round(10.3421,-1)
# 10.0

round(10.3421,-2)
# 0.0

# ---------------------------trunc ---------------------

# simply removes the elements after the decimals.
import math 

math.trunc(10.3421)
# 10

# -------------------------------pow---------------------

pow(2,3)
# 8

# -----------------------------divmod---------------------

# note : Its does first_parameter // second parameter.
# returns both quotient and remainder
# returns tuple (q,r)
divmod(20,10)
#(2,0)

divmod(100,7)
# (14,2)

# ----------------------------bin--------------------------

# any integer value can be converted to binary
bin(20)
# '0b10100'
# 0b indicates that its binary number and 
# after that everything is the actual binary converted number

bin(36)
# '0b100100'
# after 0b first 1 will always come 

# sum takes argument at iterable
sum((10,20))
# 30

# range function returns range object
# range object is an iterable object

range(10)
# range(0,10)

# Note in the range function , the lower limit is considered , but the upper limit is ignored.





