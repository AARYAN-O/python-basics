# strings are immutable

s="dshd"

s[1]='x'

# error 
# reason : strings are immutable

s1="Welcome to Deloitte"

s1[0]
# W

s1[-1]
# e

s1[1:]
# elcome to Deloitte

s1[:4]
# Welc

s1[0:8:2]
# Wloe

# s1[::] -> means that start is 0 and end is the last value

s1[:10]
# Welcome to
