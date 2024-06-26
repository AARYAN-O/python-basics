# What are default parameters ? 
# default parameters are the parameters that have default values on them , when no value is assigned to them.


# all the times, the default parameters should be at the end 
# if you do not keep them at end , then you will receive an error.
def summ(num1,num2=30):
    print(num1+num2)
    
summ(12)
