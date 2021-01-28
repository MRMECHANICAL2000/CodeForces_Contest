from collections import deque
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	array=list(map(int,input().split()))
	array.sort(reverse=True)
	array=deque(array)
	count=0
	#print("array:",array)
	while array:
		x=array.popleft()
		if x>=k:
			count+=1
		else:
			while array:
				temp=x+array.pop()
				if temp>=k:
					count+=1
					break
	print(count)

	

