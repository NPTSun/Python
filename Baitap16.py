from math import *
a,b,c = map(float,input().split())
delta = b*b - 4*a*c
if delta>0:
    print('{:.4f}'.format((-b+sqrt(delta))/(2*a)))
    print('{:.4f}'.format((-b-sqrt(delta))/(2*a)))
elif delta==0:
    print('{:.4f}'.format(-b/(2*a)))
else:
    print('No Solution')
