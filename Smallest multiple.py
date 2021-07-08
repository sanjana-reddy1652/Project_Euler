'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# importing the module
import math

# function to calculate LCM
def LCM(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

# array of integers
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]
print(LCM(x))

'''
OUTPUT:
232792560

'''
