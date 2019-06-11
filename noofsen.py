y=input()
count=1
l1=['.']
for i in range(0,len(y)):
    if y[i] in l1:
        count=count+1
print(count)
