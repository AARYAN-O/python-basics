# for type conversion , we use constructors like int() , float() , bool(),etc.

a=10.5
print(int(a))

# we can convert string into integers but the string needs to be a number
b='123'
print(int(b))

# Note that since 123a is not a number in the form of strings , completely , it will show us an error.
b='123a'
print(int(b))

c=20
print(float(c))

c='123'
print(float(c))

c='123a'
print(float(c))

# -------------------------------------bool interesting 

bool('')
# false --> bool of anything empty is false.

bool(0) 
# false --> bool(0) is also false.

bool(True) 
# True 

bool(False)
# False

bool('False')
# True
