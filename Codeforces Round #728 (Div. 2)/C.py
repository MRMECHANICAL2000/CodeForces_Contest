for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	array.sort()
	ans=0
	minRechable={}
	prefixSumReverse=[0 for i in range(n+1)]
	for i in range(n-1,-1,-1):
		prefixSumReverse[i]=prefixSumReverse[i+1]+array[i]
	prefixSumReverse=prefixSumReverse[:-1]

	for i in range(1,n+1):
		minRechable[i]=array[i-1]

	#print(array)
	#print(minRechable)
	#print(prefixSumReverse)

	for idx in range(1,n-1):
		val=array[idx+1]-array[idx]
		if val<minRechable[idx+2]:
			ans-=minRechable[idx+2]
			minRechable[idx+2]=val
		else:
			ans-=val

		if idx>1:
			ans-=abs(prefixSumReverse[idx+1]-(n-idx-1)*array[idx-1])
		#print(idx,ans)
	#print(minRechable)
	print(ans)



