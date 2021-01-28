from collections import Counter
for _ in range(int(input())):
	n=input()
	binString=input()
	hashTable=Counter(binString)

	#What is the use in multiplying by 90 and //90 on the next step.
	totalRotate=hashTable['0'] -hashTable['1']#hashTable['0']*90 -hashTable['1']*90
	#val=totalRotate//90
	#val=val%4 if -3>val or val>3  else val
	val=totalRotate%4 if -3>totalRotate or totalRotate>3  else totalRotate

	ClockRotate=["E","S","W","N"]
	AntiClockRotate=["E","N","W","S"]
	#print(val,totalRotate)
	if val<0:
		print(AntiClockRotate[abs(val)])
	else:
		print(ClockRotate[abs(val)])
