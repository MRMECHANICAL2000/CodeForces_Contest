import math
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	array=set(map(int,input().split()))
	if k==0:
		print(n)
		continue
	maxx=max(array)
	for i in range(0,maxx+2):
		if i not in array:
			mexx=i
			break
	newEle=math.ceil((maxx+mexx)/2)
	#array.add(newEle)
	if newEle==mexx:
		print(len(array)+k)
	else:
		array.add(newEle)
		print(len(array))
