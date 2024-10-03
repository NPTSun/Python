import math
a = int(input())
if a>3:
    x= pow(a,3) + 2*pow(a,2) + 5*a
elif a<1:
    x= 5*a - 8
else:
   x = pow(a,2) - 2*a + 4
print(x)
