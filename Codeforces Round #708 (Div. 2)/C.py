from collections import defaultdict
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    if n%2!=0:
        print(*[1,n//2,n//2])
    else:
        div=n//2
        if div%2!=0:
            print(*[2,2*(div//2),2*(div//2)])
        else:
            print(*[div,div//2,div//2])
