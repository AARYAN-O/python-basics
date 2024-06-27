# Object functions are id,type and isinstance
# The return type of isinstance() will be true or false depending on whether the object belongs to that class

# id :

a=12
b=a
c=14

print(id(a))
print(id(b))
print(id(c))

# 140367701787216
# 140367701787216
# 140367701787280

# type():

# already discussed.

# isinstance():

a=10
isinstance(a,int)
# true

b=20.0
isinstance(b,float)
# true

c='sr'
isinstance(c,str)
# true

lst=[1,2]
isinstance(lst,list)
# true 

st={1,2}
isinstance(st,set)
# true 

tp=(1,2,3,4)
isinstance(tp,tuple)
# true

diction={'a':1,'b':2}
isinstance(diction,dict)
# true 
