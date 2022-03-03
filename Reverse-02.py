'''
test: 
    2
    2
    0
Output : 0


test: 
    24
    2
    2
Output : 24

test: 
    7
    7
    95
Output : 95

'''

a = int(input())
b = int(input())
c = int(input())

if a==b:
    print(c)
elif a==c:
    print(b)
else:
    print(a)
