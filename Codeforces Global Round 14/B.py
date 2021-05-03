for _ in range(int(input())):
	n=int(input())
	original=n
	if n%2!=0:
		print("NO")
		continue

	for i in [2,4]:
		val=1
		n=original
		while n>0:
			n-=i*val
			val+=2
		if n==0:
			print("YES")
			break

	else:
		print("NO")

