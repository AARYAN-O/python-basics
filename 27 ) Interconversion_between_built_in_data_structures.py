# amongst list,set and tuple interconversion is always possible

# dictionaries need nested lists, nested tuples and nested sets it seems!

lst=[1,2]
tp=(1,2,3,4)
st={1,2,3,4,5,6}
print(list(tp))
print(list(st))
print(tuple(lst))
print(tuple(st))
print(set(lst))
print(set(tp))
