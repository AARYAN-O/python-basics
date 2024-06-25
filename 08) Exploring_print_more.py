# sep vs end 

print("a","b","c","d",sep="@")

# Note sep only works in between the elements and not after the last element or before the first element.
# Output:
# a@b@c@d

print("a","b","c","d",end="@")

# Output:
# abcd@
