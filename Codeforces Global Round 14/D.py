from collections import defaultdict
for _ in range(int(input())):
	n,l,r=list(map(int,input().split()))
	colour=list(map(int,input().split()))
	left=colour[:l]
	right=colour[l:]
	LeftHT=defaultdict(int)
	rightHT=defaultdict(int)
	for i in left:
		LeftHT[i]+=1
	for i in right:
		rightHT[i]+=1
	#print(LeftHT,rightHT)
	needLeft=[]
	needRight=[]
	for i in LeftHT.keys():
		if i in rightHT and rightHT[i]:
			minVal=min(rightHT[i],LeftHT[i])
			rightHT[i]-=minVal
			LeftHT[i]-=minVal

			if rightHT[i]==0:
				needRight.append(i)

			if LeftHT[i]==0:
				needLeft.append(i)

	for i in needLeft:
		del LeftHT[i]
	for i in needRight:
		del rightHT[i]
	#print(LeftHT,rightHT)

	if sum(LeftHT.values())==sum(rightHT.values()):
		print(sum(LeftHT.values()))
	elif sum(LeftHT.values())>sum(rightHT.values()):

		changeVal=sum(LeftHT.values())-sum(rightHT.values())
		need=[]
		count=0
		for i in LeftHT.keys():
			if LeftHT[i] and LeftHT[i]>=2:
				minVal=min(changeVal,2*(LeftHT[i]//2))
				count+=minVal//2
				changeVal-=minVal
				LeftHT[i]-=minVal
				if changeVal==0:
					break
				if LeftHT[i]==0:
					need.append(i)
		for i in need:
			del LeftHT[i]

		print(max(sum(LeftHT.values()),sum(rightHT.values()))+count)
	else:
		changeVal=sum(rightHT.values())-sum(LeftHT.values())
		need=[]
		count=0
		for i in rightHT.keys():
			if rightHT[i] and rightHT[i]>=2:
				minVal=min(changeVal,2*(rightHT[i]//2))
				count+=minVal//2
				changeVal-=minVal
				rightHT[i]-=minVal
				if rightHT[i]==0:
					need.append(i)
				if changeVal==0:
					break
		for i in need:
			del rightHT[i]

		print(max(sum(LeftHT.values()),sum(rightHT.values()))+count)
	#print(LeftHT,rightHT)








"""from collections import defaultdict
for _ in range(int(input())):
	n,l,r=list(map(int,input().split()))
	colour=list(map(int,input().split()))
	left=colour[:l]
	right=colour[l:]
	LeftHT=defaultdict(int)
	rightHT=defaultdict(int)
	for i in left:
		LeftHT[i]+=1
	for i in right:
		rightHT[i]+=1
	#print(LeftHT,rightHT)
	needLeft=[]
	needRight=[]
	for i in LeftHT.keys():
		if i in rightHT and rightHT[i]:
			minVal=min(rightHT[i],LeftHT[i])
			rightHT[i]-=minVal
			LeftHT[i]-=minVal

			if rightHT[i]==0:
				needRight.append(i)

			if LeftHT[i]==0:
				needLeft.append(i)

	for i in needLeft:
		del LeftHT[i]
	for i in needRight:
		del rightHT[i]
	#print(LeftHT,rightHT)

	if sum(LeftHT.values())==sum(rightHT.values()):
		print(sum(LeftHT.values()))
	elif sum(LeftHT.values())>sum(rightHT.values()):

		changeVal=sum(LeftHT.values())-sum(rightHT.values())
		need=[]
		count=0
		for i in LeftHT.keys():
			if LeftHT[i] and LeftHT[i]>=2:
				minVal=min(changeVal,LeftHT[i]//2)
				count+=minVal//2
				changeVal-=minVal
				LeftHT[i]-=minVal
				if changeVal==0:
					break
				if LeftHT[i]==0:
					need.append(i)
		for i in need:
			del LeftHT[i]

		print(max(sum(LeftHT.values()),sum(rightHT.values()))+count)
	else:
		changeVal=sum(rightHT.values())-sum(LeftHT.values())
		need=[]
		count=0
		for i in rightHT.keys():
			if rightHT[i] and rightHT[i]>=2:
				minVal=min(changeVal,rightHT[i]//2)
				count+=minVal//2
				changeVal-=minVal
				rightHT[i]-=minVal
				if rightHT[i]==0:
					need.append(i)
				if changeVal==0:
					break
		for i in need:
			del rightHT[i]

		print(max(sum(LeftHT.values()),sum(rightHT.values()))+count)
	#print(LeftHT,rightHT)







"""