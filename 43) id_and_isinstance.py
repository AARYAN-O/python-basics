# every object in python gets an id assigned to it.
# Note that lists are heterogeneous

# id():

a=[12,14]

b=a

if id(a)==id(b0:
  print("True")
else: 
  print("False")

# True

# Note : After each run the id of a and b will keep on changing continously
# but even if they change they will have the same ids anyways.

# isintance():

# Python isinstance() function returns True if the object is of specified 
# types, and if it does not match then returns False


l1=[12]

print(isinstance(l1,list))
# True 

print(isinstance(l1,tuple))
# False

# Note: The return type of isinstance is Boolean value
