r=int(input())
fl=0
for i in range(2,r-1):
    if(r%i==0):
        fl=1 
if(fl==1):
    print("yes")
else:
    print("no")
