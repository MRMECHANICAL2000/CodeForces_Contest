n,t=list(map(int,input().split()))
k=int(input())
left=1
right=n
ans=None
while left<right:
	mid=left+(right-left)//2
	print("? {} {}".format(1,int(mid)))
	ask=int(input())
	if mid-ask>=k:
		right=mid

	else:
		left=mid+1
print("! {}".format(left))

