v=list(map(int,input().split()))
h=list(map(int,input().split()))
g=v[1]
count=0
for i in range(0,len(h)):
    if(h[i]==g):
        count=count+1 
print(count)
