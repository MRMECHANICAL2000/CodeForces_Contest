for _ in range(int(input())):
	n=int(input())
	count=0
	if n%2050==0:
		for i in range(19,-1,-1):
			if i<=n:
				possible=n//(2050*(10**i))
				count+=possible
				n-=possible*(2050*(10**i))
			else:
				break
		print(count)
			
	else:
		print(-1)

