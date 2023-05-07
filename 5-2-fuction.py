def p(posInt: int):
    sum_factors=0
    for k in range(1, posInt//2+1):
        if posInt%k == 0:
            sum_factors +=k
            
    if sum_factors == posInt:
        return True
    else:
        return False
            
upper_bound = int(input())

for i in range(1,upper_bound+1):
    if p(i):
        print(i,end=' ')
