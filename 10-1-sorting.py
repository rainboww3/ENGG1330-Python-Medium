def bub(data):
    n=len(data)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if data[j-1]>data[j]:
                data[j-1], data[j]=data[j],data[j-1]
                
s=input().split(' ')
data=[int(a)for a in s]

bub(data)

for k in data:
    print(k,end=' ')

    
