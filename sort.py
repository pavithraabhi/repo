u=int(input())
o=list(map(int,input().split()))
for i in range(u):
    for j in range(u-i-1):
        if(o[j]>o[j+1]):
            o[j],o[j+1]=o[j+1],o[j]
print(" ".join(map(str,o)))
