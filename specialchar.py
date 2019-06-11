j=input()
l=['!','@','#','$','%','^','&','*','(',')','.',':','[',']']
count=0
for i in range(0,len(j)):
    if j[i] in l:
        count=count+1
print(count)
