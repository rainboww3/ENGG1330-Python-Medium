n=int(input())

count=0

if n>=0:
    for k in range(2, n//2+1):
        if n%k==0:
            count+=1
    print(count)    

else:
    print("Error: Negative number")
