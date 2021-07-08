'''
Sum square difference
'''
sum=0
sqsum=0
for i in range(1,101):
    sum=sum+i
sq=sum**2
for i in range(1,101):
    sqsum=sqsum+i**2
x=sqsum
print(sq-x)

'''
OUTPUT:
25164150

BY SANJANA
LANGUAGE: Python

'''
