```
The program:
Your program must read two numbers and output the concatenation of their difference and sum.

INPUT:
Two positive integers A and B.

OUTPUT:
The concatenated results of A-B and A+B.
```

a, b = [int(i) for i in input().split()]
print(str(a-b)+str(a+b))
