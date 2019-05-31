k=list(map(str,input().split()))
b=k[0]
c=k[1]
if(len(b)==len(c)):
    print(b or c)
elif(b>c):
    print(b)
else:
    print(c)
