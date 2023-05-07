import sys

a=[0]
del a[0]
n=int(input())
m=0
i=0
j=0
b=range(n)

for k in b:
    x=0
    b=[]
    i,j=input().split() 
    v=int(i)
    w=int(j)
    a.append([v,w])                              

ans='Attack'
bans="Safe"
def command1():
    print(ans)
    sys.exit()
    return
    
for k in a:
    l=0
    i=[]
    j=[]
    i=k[0+0]
    j=k[0+1]
    m=m+1
    
    def command2():
        print(bans)
        sys.exit()
        return
        
    for l in a[0+m:]:
        x=0
        y=0
        if m<0:
            sys.exit()
            
        q=l[0+0]
        p=l[0+1]
        ans='Attack'
        bans='Safe'
        if i==q:   
            command1()
        if j==p:   
            command1()
        if i-j==q-p:  
            command1()
        if i+j==q+p:
            command1()
             
    command2()

sys.exit()







