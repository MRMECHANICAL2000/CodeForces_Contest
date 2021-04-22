from collections import Counter
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	array=list(map(int,input().split()))
	i=0
	while k and i<n:
		if array[i]>0:
			if array[i]<=k:
				temp=array[i]
				k-=temp
				array[i]=0
				array[-1]+=temp
			else:
				array[i]-=k
				array[-1]+=k
				k=0
		i+=1
	print(*array)