for _ in range(int(input())):
	n=input()
	hashSet=set()
	prev=None
	for i in input():
		if prev==None:
			prev=i

		if i not in hashSet:
			hashSet.add(i)
		elif prev!=i:
			print("NO")
			break
		prev=i
	else:
		print("YES")