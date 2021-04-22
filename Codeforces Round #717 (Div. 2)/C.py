from functools import lru_cache
	
def gcd(a,b):
	if b==0:
		return(a)
	return(gcd(b,a%b))

@lru_cache(None)
def subsetSum(curSum,totalSum,idx,array):

	if idx>=len(array):
		return(False)

	if totalSum==2*curSum:
		return(True)

	if 2*curSum>totalSum:
		return(False)
	withVal=subsetSum(curSum+array[idx],totalSum,idx+1,array)
	if withVal:
		return(True)	
	withOutVal=subsetSum(curSum,totalSum,idx+1,array)

	return(withOutVal)


n=int(input())
array=tuple(map(int,input().split()))
totalSum=sum(array)

if totalSum%2!=0 or  not subsetSum(0,totalSum,0,array):
	print(0)

else:
	for idx,val in enumerate(array):
		if val%2!=0:
			print(1)
			print(idx+1)
			break
	else:
		ansIdx=0
		ansCount=float('inf')
		for idx,val in enumerate(array):
			count=0
			while val%2==0:
				count+=1
				val=val/2
			if count<ansCount:
				ansCount=count
				ansIdx=idx
		print(1)
		print(ansIdx+1)





