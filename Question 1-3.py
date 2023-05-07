a =  input().split()
b =  input().split()
c=a+b
c=list(map(int,c)) 
d=sorted(c)

if len(d)%2==0:
    x=0
    x=len(d)/2
    a=d[0:int(x)]
    b=d[int(x):] 
    
if len(d)%2==1:
    x=0
    x=float(x)
    x=len(d)/2-0.5
    a=d[0:int(x)]
    b=d[int(x):]      

if len(d)%2==1:
    x=0
    x=float(x)
    x=len(d)/2+0.5
    m=d[0:int(x)]
    n=d[int(x):]

asum=0 
aavg=0 

for i in a:
    asum+=i 

aa=len(a)
aavg=asum/aa

asome=0 
asumm=0 

for i in a:
    asome=(i-aavg)*(i-aavg)
    asumm+=asome
    
bsum=0 
bavg=0 

for i in b:
    bsum+=i 

bb=len(b)
bavg=bsum/bb

bsome=0 
bsumm=0 

for i in b:
    bsome=(i-bavg)*(i-bavg)
    bsumm+=bsome

if len(d)%2==1:
    msum=0
    mavg=0

    for i in m:
        msum+=i

    mm=len(m)
    mavg=msum/mm

    msome=0
    msumm=0

    for i in m:
        msome=(i-mavg)*(i-mavg)
        msumm+=msome

if len(d)%2==1:
    nsum=0
    navg=0

    for i in n:
        nsum+=i

    nn=len(n)
    navg=nsum/nn

    nsome=0
    nsumm=0

    for i in n:
        nsome=(i-navg)*(i-navg)
        nsumm+=nsome
    
if len(d)%2==1:    
    mans=0
    mans=msumm+nsumm
    
ans=0 
ans=asumm+bsumm

print("%.2f" %ans)

print("[",end='')

for i in a:
    print(i,"",end='')
    
print("]",end='')    
    
print("[",end='')

for i in b:
    print(i,"",end='')
    
print("]")     

if len(d)%2==1:
    if mans==ans:
        print("[",end='')

        for i in m:
            print(i,"",end='')
    
        print("]",end='')    
    
        print("[",end='')

        for i in n:
            print(i,"",end='')
    
        print("]") 




