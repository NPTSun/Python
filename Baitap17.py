from math import *
m,n = map(int,input().split())
if m%n==0 or n%m==0:
    print('Yes')
else:
    print('No')
