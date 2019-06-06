t=int(input())
f=0
for i in range(2,t-1):
    if(t%i==0):
        f=1 
if(f==1):
    print("no")
else:
    print("yes")
