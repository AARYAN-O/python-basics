# note : Variable arguments are only called args 
# variable arguments do not expect keyword arguments to come and hence if we put keyword arguments there , we will be getting 
# error.
# What is the meaning of variable arguements?
# It means that we can pass any number of arguments in args.

def summ(*nums):
    print(sum(nums))

summ(1)
