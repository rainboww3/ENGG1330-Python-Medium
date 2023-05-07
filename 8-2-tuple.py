list=[]

n=int(input())
for i in range(n):
    s=input()
    l=s.split()
    nist=[int(e) for e in l]
    
    for x in range(nist[0],nist[0]+nist[2]):
        for y in range(nist[1], nist[1]+nist[3]):
            if (x,y) not in list:
                list.append((x,y))
                
print(len(list))                
