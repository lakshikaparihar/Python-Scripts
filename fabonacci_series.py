```
assume 0=a , 1=b ,2=c , find the value of the string in the fabonacci series

1,1,2,3,5,8.........
for the input:
  a                     --->  1
  b                     --->  1
  e                     --->  5
```

t = input() 
f = [1,1]
l = ord(t)-97
for i in range(1,l):
    f.append(f[i-1]+f[i]) 
print(f[l])
