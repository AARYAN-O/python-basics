# Outputs can be written using +,f-strings, format and %(also called as string-interpolation)

# Note : Amongst all the above mentioned methods, the f-strings are the fastest.

# ------------------------------------------------------------------
# 1) using plus (+):

a=1
print("One is represented as "+str(a))

# -------------------------------------------------------------------
# 2) using format:

# Note : If index is not given while using format , then it means that it will follow the same order as is given inside the 
# format()

print("The animal is {} and {}".format("tiger","lion"))

# entry of the values takes in the order of the inputs
# The indexing here too starts with 0 only
print("The animal is {1} and {0}".format("tiger","lion"))

# -----------------------------------------------------------------------
# 3) f-strings:
# while we use indexes in format() , we use variables in f-strings 

name="Santosh"
age=44
print(f"The name is {name} and age is {age}")

# -------------------------------------------------------------------------
# 4) String-interpolation:

# %c , %s, %i and %d,%u,%o,%x,%X,%e,%E,%f,%g,%G

# so %s stands for string 
print("The animal is %s" %("tiger"))
# The animal is triger.


# %d stands for integers
# %d can be both positive and negative.

print("The number is %d"%(-20))
# The number is -20.

# If you use the decimals , it will still be typecasted to integers.
print("The number is %d"%(-20.6))
# The number is -20.

# %i is the same as %d.




