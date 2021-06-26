for _ in range(int(input())):
	n=int(input())
	array=[(val,idx) for idx,val in enumerate(list(map(int,input().split())),1)]
	array.sort()
	ans=0
	for i in range(n):
		for j in range(i+1,n):
			i_start_j=array[i][0]*array[j][0]
			i_plus_j=array[i][1]+array[j][1]
			if i_start_j==i_plus_j:
				ans+=1
			if i_start_j>(4*n)-1:
				break
	print(ans)

