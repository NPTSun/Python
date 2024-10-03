import math
a, b, alpha = map(float,input().split())
pi = 3.14159
s = 0.5 * a * b * math.sin((alpha*pi/180))
print('{:.2f}'.format(s))
