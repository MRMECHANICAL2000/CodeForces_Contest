from collections import defaultdict
def forThreeNumbers(n,k):
    if n%2!=0:
        return([1,n//2,n//2])
    else:
        div=n//2
        if div%2!=0:
            return([2,2*(div//2),2*(div//2)])
        else:
            return([div,div//2,div//2])


for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	ans=forThreeNumbers(n-(k-3),3)
	for i in range(k-3):
		ans.append(1)
	print(*ans)
