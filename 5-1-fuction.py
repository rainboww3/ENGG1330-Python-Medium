def a(size: int):
    for i in range(0,size):
        for j in range(0,size):
            if(i==0 or i==size-1 or j==0 or j==size-1):
                print('#',end='')
            else:
                print(' ',end='')
        print()        
        
def b(size: int):
    for i in range(0,size):
        for j in range(0,size):
            if(i==0 or i==size-1 or i==j):
                print('#',end='')
            else:
                print(' ',end='')
        print()        


def c(size: int):
    for i in range(0,size):
        for j in range(0,size):
            if(i==0 or i==size-1 or i==size-1-j):
                print('#',end='')
            else:
                print(' ',end='')
        print()        
        

def d(size: int):
    for i in range(0,size):
        for j in range(0,size):
            if(i==0 or i==size-1 or i==j or i==size-1-j):
                print('#',end='')
            else:
                print(' ',end='')
        print()                


pattern=str(input())
n=int(input())


if pattern =='a':
    a(n)
elif pattern == 'b':
    b(n)
elif pattern == 'c':
    c(n)
elif pattern == 'd':
    d(n)    

