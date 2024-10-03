from math import *
a,b,c = map(float,input().split())
t = 10**-9
if abs(a-b)<t and abs(b-c)<t:
    print('Tam giac deu')
elif abs(a-b)<t or abs(c-b)<t or abs(a-c)<t:
    print('Tam giac can')
else:
    print('Tam giac thuong')
