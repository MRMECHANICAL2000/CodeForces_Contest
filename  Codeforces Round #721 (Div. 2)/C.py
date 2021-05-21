#Optimal Approach
from collections import defaultdict
for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	hashTable=defaultdict(list)
	ans=0
	for idx,val in enumerate(array,1):
		hashTable[val].append(idx)

	for i in hashTable:
		prefixSum=0
		for j in hashTable[i]:
			ans+=prefixSum*(n-j+1)
			prefixSum+=j
	print(ans)




#Brute Force Method
"""
def solve(array,k): 
	global ans
	temp=0
	hashTable={}
	start=0
	for i in range(k):
		i=array[i]
		if i not in hashTable:
			hashTable[i]=0
		hashTable[i]+=1
		val=hashTable[i]
		temp+=val*(val-1)//2
		temp-=(val-1)*(val-2)//2
	ans+=temp

	for i in range(k,len(array)):
		val=hashTable[array[start]]
		temp-=val*(val-1)//2
		temp+=(val-1)*(val-2)//2
		hashTable[array[start]]-=1

		i=array[i]
		if i not in hashTable:
			hashTable[i]=0
		hashTable[i]+=1
		val=hashTable[i]
		temp+=val*(val-1)//2
		temp-=(val-1)*(val-2)//2
		start+=1
		ans+=temp
		#print(hashTable)
	#print(k,temp,ans)

for _ in range(int(input())):
	n=int(input())
	ans=0
	array=list(map(int,input().split()))
	for i in range(2,n+1):

		solve(array,i)
	print(ans)"""