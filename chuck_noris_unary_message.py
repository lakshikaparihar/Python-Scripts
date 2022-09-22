'''
Binary with 0 and 1 is good, but binary with only 0, or almost, is even better! Originally, this is a concept designed by Chuck Norris to send so called unary messages.

Write a program that takes an incoming message as input and displays as output the message encoded using Chuck Norris’ method.

Here is the encoding principle:

The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
- Second block: the number of 0 in this block is the number of bits in the series
  
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

count=0
f = [bin(ord(i)).replace('0b','') for i in list(message)]
for i in range(len(f)):
    if len(f[i])!=7:
        f[i] = str("0"*(7-len(f[i])))+f[i]
f = ''.join(f)

k = f[0]
count=0

for i in f:

    if k==i:
        count+=1
    else:
        print((["0","00"][k=='0']),"0"*count,end=" ")
        k = i
        count=1
print((["0","00"][i=='0']),"0"*count,end="")
