from math import *
a,b,c,x,y = map(int,input().split())
if (a<=x and b<=y) or (b<=x and c<=y) or (a<=x and c<=y) or (a<=y and c<=x):
    print('Yes')
else:
    print('No')
