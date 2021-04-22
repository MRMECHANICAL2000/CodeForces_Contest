from collections import deque
for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	totalXOR=0
	for i in array:
		totalXOR^=i
	if totalXOR==0:
		print("YES")
	else:
		left=0
		right=0
		leftIdx=0
		rightIdx=n-1

		for i in array:
			left^=i
			if left==totalXOR:
				break
			leftIdx+=1

		for i in array[::-1]:
			right^=i
			if right==totalXOR:
				break
			rightIdx-=1

		if leftIdx<rightIdx:
			print("YES")
		else:
			print("NO")


