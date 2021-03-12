import math
for _ in range(int(input())):
	n=int(input())
	minor=[]
	dimond=[]
	for i in range(2*n):
		x,y=list(map(int,input().split()))
		if x==0:
			minor.append(abs(y))
		else:
			dimond.append(abs(x))
	minor.sort()
	dimond.sort()
	ans=0
	for i in range(n):
		ans+=math.sqrt(minor[i]**2+dimond[i]**2)
	print(ans)

