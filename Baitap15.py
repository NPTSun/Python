from math import *
a,b,c = map(float,input().split())
if (a+b>c and a+c>b and b+c>a):
    p = (a+b+c)/2
    heron = sqrt(p*(p-a)*(p-b)*(p-c))
    print('{:.4f}'.format(heron))
else:
    print('No Solution')
