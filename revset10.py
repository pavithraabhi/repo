t=int(input())
re=0
while(t>0):
    d=t%10
    re=re*10+d  
    t=t//10
print(re)
