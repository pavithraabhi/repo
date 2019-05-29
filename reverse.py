p=int(input())
c=0
while(p>0):
    v=p%10
    c=c*10+v
    p=p//10
print(c)
