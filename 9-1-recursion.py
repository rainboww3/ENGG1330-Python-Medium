

def e(n):
    for i in range(1,n+1):
        if i%2==0:
            print("f{i}",end=" ")

def ev(n):
    if n==0:
        return
    if n%2==0:
        print(n,end=' ')
        
    ev(n-1)


n=int(input())
ev(n)
    
