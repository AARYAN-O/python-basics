# slicing and indexing is allowed in lists.
# lists are mutable too.

l1=[1,2,3,4,'abc']
# list is non-homogeneous

l1[1:4]
# [2,3,4]

l1[1:10]
# [2,3,4,'abc']

l1[10]
# error will come here saying that list index out of range.

l1[0]=6
# [6,2,3,4,'abc']

# negative indexing is also allowed in lists 
l1[-2]
# 4

l1[0:4]
# [6,2,3,4]

l1[4:0]
# wont give error in this case .
# Rather empty list will get returned

l1[4:0:-1]
# ['abc',4,3,2]

l1[::-1]
# ['abc',4,3,2,6]

# the last parameter in indexing is called as the step parameter.
l1[1::-2]
# if we dont specify the first parameter , it starts with 0
# if we dont specify the last parameter , it end with last 
# [2]

l1[2:]
# [3,4,'abc']

l1[:2]
# [6,2]


