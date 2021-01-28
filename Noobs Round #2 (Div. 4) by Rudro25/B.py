from collections import Counter
for _ in range(int(input())):
	n=input()
	array=list(map(int,input().split()))
	odd=0
	even=0
	for i in array:
		if i%2==0:
			even+=1
		else:
			odd+=1
	if odd:
		print(even)
	else:
		print(-1)