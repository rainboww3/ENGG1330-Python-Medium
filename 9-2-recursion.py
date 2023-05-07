

def ip(n):
    for i in range(2,n):
        if n%i==0:
            return print('false')
    return print('true')
    
def il(n,x):
    if n==1:
        return print('true')
    if x%n==0:
        return print('false')
    il(n-1,x)


n=int(input())
il(n-1,n)
