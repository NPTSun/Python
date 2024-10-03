from math import *
a,b = map(int,input().split())
if a==0:
    if b==0:
        print('Many Solutions')
    else:
        print('No Solution')
else:
    x = -b/a
    print('{:.2f}'.format(x))
