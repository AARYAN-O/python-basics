# we can have args and kwargs in the same function as well.
# we just need to ensure that the kwargs/args in the function definition should have the same order as kwargs and args in the 
# function calling .Also note that the kwargs/keyword arguments in the function call/defintion should always be 
# written after the args/positional argument.

def emp_info(*ratings,**data):
    print(type(data))
    print(data)
    print()
    print(type(ratings))
    print(ratings)
    
emp_info(4.2,4.6,4.8,city="Hyd",empno=1001)

# note : When we print the type of ratings, it will be tuple 
# note : When we print the type of data , it will be dictionary.


# output:

<class 'dict'>
{'city': 'Hyd', 'empno': 1001}

<class 'tuple'>
(4.2, 4.6, 4.8)
