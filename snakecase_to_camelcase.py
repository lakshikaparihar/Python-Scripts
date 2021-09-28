import sys
import math

variable_name = input()
variable_name = list(variable_name)

for i in range(len(variable_name)-1):
    if variable_name[i]=="_":
        variable_name[i+1]=variable_name[i+1].upper()
print(''.join(variable_name).replace("_",""))
