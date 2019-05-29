b=int(input())
g=0
while(b>0):
    d=b%10
    g=g+d**2
    b=b//10
print(g)
