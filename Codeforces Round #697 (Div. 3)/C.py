from collections import defaultdict
for _ in range(int(input())):
	a,b,n=list(map(int,input().split()))
	BoyHash=defaultdict(int)
	GirlHash=defaultdict(int)
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))	
	for i in range(n):
		BoyHash[A[i]]+=1
		GirlHash[B[i]]+=1
	ans=0
	for i in range(n):
		ans+=n-BoyHash[A[i]]-GirlHash[B[i]]+1
	print(ans//2)
