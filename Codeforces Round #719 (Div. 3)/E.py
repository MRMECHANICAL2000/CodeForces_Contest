from collections import defaultdict
for _ in range(int(input())):
	n=int(input())
	string=input()
	left=[0]
	right=[0]
	count=0
	for i in string:
		if i=="*":
			left.append(left[-1])
			count+=1

		else:
			left.append(left[-1]+count)

	count=0
	for i in string[::-1]:
		if i=="*":
			right.append(right[-1])
			count+=1
		else:
			right.append(right[-1]+count)
			
	left=left[1:]
	right=right[1:]
	right=right[::-1]
	ans=min(right[0],left[-1])
	for i in range(n-1):
		ans=min(ans,left[i]+right[i+1])
	print(ans)

