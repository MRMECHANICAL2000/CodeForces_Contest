import math
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	string=input()
	if 2*k==n:
		print("NO")
	elif k==0 or string[:k]==string[::-1][:k]:
		print("YES")
	else:
		print("NO")



