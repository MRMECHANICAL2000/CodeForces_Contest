for _ in range(int(input())):
    r,b,d=list(map(int,input().split()))
    if (abs(r-b)/min(r,b))>d:
    	print("NO")
    else:
    	print("YES")

