from math import *
a,b,c = map(int,input().split())
if a==b and a==c:
    print('Tam giac deu')
elif (a==b and a!=c) or (b==c and b!=a) or (a==c and c!=b):
    print('Tam giac can')
else:
    print('Tam giac thuong')
