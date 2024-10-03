import math
a = float(input())
if a==-3.0:
     print('Div by zero')
else:
    if a>0:
         x = pow(a,2) + math.sqrt(a) + 1
         print('{:.6f}'.format(x))
    else:
         x = (pow(a,3) + 2*a + 1) / (a + 3)
         print('{:.6f}'.format(x))
