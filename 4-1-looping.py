n=int(input())

if n>=0:
    k=2
    while k<n//2+1:
        if n%k==0:
            print(k,end=" ")
        k=k+1
        
else:
    print("Error: Negative number")
