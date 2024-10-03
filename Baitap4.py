a,b = map( int,input().split())
s = a%10 + b%10
p = (a//1000) * (b//1000)
print(s,'\n',p)
