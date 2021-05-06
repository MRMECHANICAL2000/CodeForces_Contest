from collections import defaultdict
for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	ans=0
	HashTable=defaultdict(int)
	for i in range(n):
		HashTable[i+1-array[i]]+=1
	for i in HashTable:
		ans+=HashTable[i]*(HashTable[i]-1)//2

	print(ans)
