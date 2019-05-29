h=int(input())
s=0
t=h 
while(h>0):
    digi=h%10
    s=s+digi*digi*digi
    h=h//10
if(s==t):
    print("yes")
else:
    print("no")
   
