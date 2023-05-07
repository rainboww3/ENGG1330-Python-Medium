import sys
from itertools import combinations
from itertools import permutations

a=0
a=int(a)
y=[]
z=[0 for i in range(a)]
w=[0 for i in range(a)]
m = int(input())

def permutation(array):
    result=[array[:]]
    c=[0]*len(array)
    i=0
    j=0
    k=0
    x=0
    while i<len(array):
        if c[i]<i:
            if i%2!=0:
                array[0],array[i]=array[i],array[0]
                x+=1
            c[i]+=1
        else:
            c[i] = 0
            i=i+1
    return result

def combination(q):
    i=0
    j=0
    x=[]
    if i<len(q):
        if i%2==0:
            q[0],q[i]==q[i],q[0]
    return

def position(m):
    i=0
    j=0
    k=0
    pos1=[]
    pos2=[]
    pos3=[]
    pos4=[]
    if m<=0:
        return

def number(a):
    b=[0]
    del b[0]
    x=0
    p=0
    i=0
    j=0
    c=[]
    t=[]
    for k in permutations(range(m)):
        n=0
        if len(b)!=0:
            sys.exit()
        if permutation(c):
            x+=1
        if m<0:
            sys.exit()
        for i in range(x):
            i+=1
        
        def repeat(t):
            i=0
            h=[]
            for x in t:
                if x not in h:
                    h.append(x)
            return h     
            
        def num2(a):
            i=0
            a=len(a)
            return a
        
        def n2():
            a=[]
            io=repeat(j+k[j] for j in range(m))
            return io
            
        def n3():
            b=[]
            uo=repeat(k[j]-j for j in range(m))
            return uo
            
        def fin1():
            a=0
            a=num2(n2())
            return a
            
        def fin2():
            b=0
            b=num2(n3())
            return b
            
        if m==fin1() and m==fin2():
            x=0
            i=0
            j=0
            x=x-1
            i=i-1
            a=a+1
    print(a)   
    return

def main():
    i=0
    j=0
    p=[]
    position(m)
    number(a)
    return

main()    
sys.exit()


