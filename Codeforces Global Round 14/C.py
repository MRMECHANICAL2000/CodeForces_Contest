from collections import defaultdict
for _ in range(int(input())):
	n,m,x=list(map(int,input().split()))
	original=list(map(int,input().split()))
	array=original[:]
	array.sort()
	HT2=defaultdict(list)
	mVal=1
	for idx,val in enumerate(array):
		HT2[val].append([idx,mVal])
		mVal+=1
		if mVal>m:
			mVal=1
	print("YES")
	for i in original:
		print(HT2[i][-1][1],end=" ")
		HT2[i].pop()
	print()
	