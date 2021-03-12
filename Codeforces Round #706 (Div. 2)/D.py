n=int(input())
array=list(map(int,input().split()))
leftToRight=[0 for i in range(n)]
rightToLeft=[0 for i in range(n)]

for i in range(1,n):
	if array[i-1]<array[i]:
		leftToRight[i]=leftToRight[i-1]+1

for i in range(n-2,-1,-1):
	if array[i+1]<array[i]:
		rightToLeft[i]=rightToLeft[i+1]+1

maxVal=max(max(leftToRight),max(rightToLeft))
maxCount=0
maxOnSameIdx=0
for i in range(n):
	if leftToRight[i]==maxVal:
		maxCount+=1
	if rightToLeft[i]==maxVal:
		maxCount+=1
	if leftToRight[i]==maxVal and rightToLeft[i]==maxVal:
		maxOnSameIdx+=1

if maxCount==2 and maxOnSameIdx==1 and maxVal%2==0:
	print(1)
else:
	print(0)

