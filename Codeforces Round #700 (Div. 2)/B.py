import math
for _ in range(int(input())):
	heroAttack,heroHeath,n=list(map(int,input().split()))
	monsterAttack=list(map(int,input().split()))
	monsterHealth=list(map(int,input().split()))
	monster=[]
	for i in range(n):
		monster.append([monsterAttack[i],monsterHealth[i]])
	monster.sort()
	
	idx=0
	while idx<len(monster)-1:
		mA=monster[idx][0]
		mH=monster[idx][1]

		attackReq=math.ceil(mH/heroAttack)

		heroHeath-=mA*attackReq
		mH-=heroAttack*attackReq

		if mH<=0:
			idx+=1
	heroHeath-=monster[-1][0]*(math.ceil(monster[-1][1]/heroAttack)-1)
	monster[-1][1]-=heroAttack*(math.ceil(monster[-1][1]/heroAttack)-1)

	if heroHeath>0 and heroAttack>=monster[-1][1]:
		print("YES")
	else:
		print("NO")