# map(func,iterable)
# here we are applying the function to each and every iterable

# note that while we are using map() to pass the inputs from the functions , we need to have a return statement .
# Otherwise, it will do nothing 
def func(a):
    return a*a

lst=[1,2,3,4]
x=list(map(func,lst))
# map function returns map object and filter function returns filter object
x
