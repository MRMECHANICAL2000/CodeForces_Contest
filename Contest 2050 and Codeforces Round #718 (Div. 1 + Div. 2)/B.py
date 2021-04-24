import heapq
from collections import defaultdict
for _ in range(int(input())):
	n,m=list(map(int,input().split()))
	TrackTable=defaultdict(dict)
	Player=defaultdict(dict)
	lengthHeap=[]
	for i in range(n):
		length=list(map(int,input().split()))
		#TrackTable[i]=length
		for j in length:
			if j not in TrackTable[i]:
				TrackTable[i][j]=0
			TrackTable[i][j]+=1
			heapq.heappush(lengthHeap,(j,i))
	#print(TrackTable)

	for i in range(m):
		x,y=heapq.heappop(lengthHeap)
		TrackTable[y][x]-=1
		Player[i][y]=x
	#print(TrackTable)

	for i in range(m):
		for j in range(n):
			if j not in Player[i]:
				for x in TrackTable[j]:
					if TrackTable[j][x]:
						TrackTable[j][x]-=1
						Player[i][j]=x
						break

	#print(TrackTable)

	#for i in range(m):
	#print(Player)

	for i in range(n):
		for j in range(m):
			print(Player[j][i],end=" ")
		print()
