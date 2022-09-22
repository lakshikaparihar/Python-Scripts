'''
We are given two integers a and b. For those two integers we look for positive integers which divide both a and b (without leaving a remainder). 
If there does not exist such an integer besides 1, we call a and b coprime.
'''

import sys
import math

a = int(input())
b = int(input())
if math.gcd(a,b) != 1:
    print("false")
else: print("true")
