n=int(input())
oneCol=[] #col1
twoCol=[] #col2,col3

for i in range(1,n+1):
	if i%2==0:
		count=0
	else:
		count=1
	for j in range(1,n+1):
		if (count)%2!=0:
			oneCol.append([i,j])
		else:
			twoCol.append([i,j])
		count+=1
oneCol_idx=0
twoCol_idx=0
x=int(input())

if x!=1:
	col1,col2,col3=[1,2,3]
	print(col1,*oneCol[oneCol_idx])
	oneCol_idx+=1

else:
	col1,col2,col3=[2,1,3]
	print(col1,*oneCol[oneCol_idx])
	oneCol_idx+=1

for i in range(1,n*n):
	x=int(input())
	if x!=col1 and oneCol_idx<len(oneCol):
		print(col1,*oneCol[oneCol_idx])
		oneCol_idx+=1

	elif x!=col2 and twoCol_idx<len(twoCol):
		print(col2,*twoCol[twoCol_idx])
		twoCol_idx+=1

	else:
		if oneCol_idx<len(oneCol):
			print(col3,*oneCol[oneCol_idx])
			oneCol_idx+=1

		else:
			print(col3,*twoCol[twoCol_idx])
			twoCol_idx+=1
