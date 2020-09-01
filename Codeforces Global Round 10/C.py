for _ in range(int(input())):
	input()
	array=[int(i) for i in input().split()]
	ans=0
	prev=array[-1]
	for i in array[::-1]:
		if i>prev:
			ans+=(i-prev)
		prev=i

	print(ans)






