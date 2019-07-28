import math
c,f=list(map(int,input().split())) 
p=c*f 
rt=math.sqrt(p) 
if int(rt+0.5)**2==p: 
    print("yes") 
else:
    print("no")
