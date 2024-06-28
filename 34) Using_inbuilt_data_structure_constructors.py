# ------------
lst=[1,2,3,4,4]
tup=tuple(lst)
print(tup)

# --------------
st=set(lst)
print(st)

# ---------------
st={}
print(type(st))
# dictionary
# --------------

tip=(10)
print(type(tip))
# int

# --------------

tip =(10,)
print(type(tip))
# tuple

# --------------
# for dictionaries , we cannot use constructors directly.
diction=dict(lst)
print(diction)
# error

# ---------------
# whenever you use dictionary constructor , we need to use the keys without the string.
diction=dict(a=1,b=2)
print(diction)
# {a:1,b:2}

# -----------------
diction=dict("a"=1,"b"=2)
print(diction)
# error

# ------------------

diction={"a":1,"b":2}
print(diction)
# error
