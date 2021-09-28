import re
t = input()
print("".join(re.findall('([A-Z])', t)))
print("".join(re.findall('([a-z])', t)))
