import math
x = float(input())
f = math.sin(x) + math.sqrt(math.log(3*x,4)) + math.ceil(3*math.exp(x))
print('{:.6f}'.format(f))
