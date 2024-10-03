import math
x,k = map(float,input().split())
c = math.sqrt(math.fabs(x))
a = math.pow(c,4) + math.pow(k,3)
f = math.pow(math.log10(a),3) + math.pow(math.cos(x),5)
print('{:.2f}'.format(f))
