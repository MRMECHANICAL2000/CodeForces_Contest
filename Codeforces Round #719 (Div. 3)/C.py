for _ in range(int(input())):
	n=int(input())
	if n==2:
		print(-1)
	else:
		matrix=[[0 for i in range(n)] for i in range(n)]
		val=1
		for i in range(n):
			for j in range(i%2,n,2):
				matrix[i][j]=val
				val+=1

		for i in range(n):
			for j in range(1 if i%2==0 else 0 , n,2):
				matrix[i][j]=val
				val+=1
		for i in matrix:
			print(*i)

