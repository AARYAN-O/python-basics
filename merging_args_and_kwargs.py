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
