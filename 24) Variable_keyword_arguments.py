# Note : Keyword arguments are also called as kwargs.
# Keyword arguments expect everything to come in the form of key-value pair.
# Try to find  its relationship with the ** Context that we use in the airflow.
# if you pass positional argument , it will give you an error since it will be expecting keyword argument

def emp_info(**data):
    print(data)

emp_info(city='Hyd',empno=1001,ename='Amit')
# this expects only keywords arguments to come.

