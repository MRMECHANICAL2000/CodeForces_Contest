for _ in range(int(input())):
    m,n,k=list(map(int,input().split()))
    if (max(n,m))*(min(n,m)-1)+(max(n,m)-1)==k:
    	print("YES")
    else:
    	print("NO")
    #print((min(n,m))*(min(n,m)-1)+(max(n,m)-1),k)
