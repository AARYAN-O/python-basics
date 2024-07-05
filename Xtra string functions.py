# if we write s.split() without collecting the values in some variable.
# nothing will happen.
# split() acutally returns a list 
# wherever the split happens , the comma inside the list will be present there

s3="welcome to to to \n to Del"
s3.split("\n")
print(s3)
# welcome to to to 
 # to Deloitte

s3="welcome to to to \n to Del"
y=s3.split("\n")
print(y)
# ['welcome to to to' ,'to Deloitte']

n=s3.splitlines()
print(n)
# ['welcome to to to ', ' to Deloitte']
