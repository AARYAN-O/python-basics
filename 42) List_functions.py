# reversing a string should be done using s[::-1]

# List functions : Append , Insert , Extend, Copy ,Count , Reverse, Remove
# Sort, Pop, Index , Clear, + 

# Append :
# adds an element at the start of the list 
lst=[]
lst.append(1)
# [1]

type(lst)
# list

# problem:
l1=[2,8,4,6]
l2=[10,12]
l1.append(l2)
print(l1)

#Insert :
# insert(index,element_to_be_inserted)

lst3=[4,5,6,7,8,9,10]

lst3.insert(7,2)
# 7th we index pe 2 de do
# [4,5,6,7,8,9,10,2]

lst3.insert(3,111)
# 3rd index pe 111 daal do 
# Note that when the element already exists on the third index,
# the new element will replace the old element at third index
# and the right shifting of the old element will happen 
# [4,5,6,111,7,8,9,10,2]

# what if we take a very large index:
# it will not give us error but will simply place the element at the last position
lst3.insert(5000,'ok')
# [4,5,6,111,7,8,9,10,2,'ok']

# Extend:
# Solution1
l1=[2,8,4,6]
l2=[10,12]
l1.extend(l2)
print(l1)
# [2, 8, 4, 6, 10, 12]
# extend function needs an iterable

# Extend function just needs an iterable inside it ...thats all

tpu=(1,2,3,4)
l1.extend(tpu)
print(l1)

# # Solution1
l1=[2,8,4,6]
l2=[10,12]
l1.extend(l2)
print(l1)
# extend function needs an iterable

# solution2
l1+l2

# There is nothing like average function in python

# How can we duplicate the contents of the list n number of times ?
l1*2
# repetition of characters

min('mobile')
# 'b'

max('mobile')
# 'o'

# Copy :

lst1=[1,2]
lst1
# [1, 2]

lstx=[]
lstx=lst1.copy()
print(lstx)
# [1,2]

lx=lst1
print(lx)
# [1,2]

# lst.copy() will create a completely new object
# l1=l2 will act with each other

l1=[10,20]
l2=l1

l1[1]=30

print(l1)
# [10,30]
print(l2)
# [10,30]

l2[1]=40

print(l1)
# [10,40]
print(l2)
# [10,40]
# l2 changes when l1 changes
# l1 also changes when l2 changes in case we case the assignment operator
# we can assume here that the equals to operator creates a pointer
# to the object.

# an important thing to note while doing this :
del l1 
# This will not delete l2 as well since only the pointer between l1 and l2
# gets deleted 
print(l1)
# object undefined error
print(l2)
# [10,40]

l4=[20,80]
l6=l4.copy()

print(l4)
# [20,80]

print(l6)
# [20,80]
# copy does not point to the same element
# So it is pretty straighforward ==> the element that is deleted 
# only gets deleted and nothing else happens







