n = int(input())
if n%2==0 and n<0 and n%3==0:
    print('No')
elif n%2==0:
    print('Yes')
elif n%3==0 and n<0:
    print('Yes')
else:
    print('No')
