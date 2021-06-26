for _ in range(int(input())):
	n=int(input())
	ans=[i for i in range(1,n+1)]
	for i in range(1,n,2):
		ans[i],ans[i-1]=ans[i-1],ans[i]

	if n%2==0:
		print(*ans)

	else:
		ans[-1],ans[-2]=ans[-2],ans[-1]
		print(*ans)
