 
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
    
ans=0 
ans=asumm+bsumm

print("%.2f" %ans)


