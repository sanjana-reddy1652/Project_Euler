'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def palin(n):
    sum=0
    temp=n
    while n!=0:
        r=n%10
        sum = sum*10+r
        n=n//10
    if(temp==sum):
        return 1
    else:
        return -1

    
n=0
for i in range(100, 1000):
   for j in range(10,i):
        if(palin(i*j)== 1 and i*j > n):
            n=i*j
print(n)

'''
OUTPUT
906609

BY SANJANA
LANGUAGE: Python

''' 
