r=list(map(int,input().split()))
x=r[0]
y=r[1]
z=r[2]
if x>y and x>z:
    print(x)
elif y>z:
    print(y)
else:
    print(z)
