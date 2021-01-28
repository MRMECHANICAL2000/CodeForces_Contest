for _ in range(int(input())):
	a,b=list(map(int,input().split()))

	if a&b==0:     #if two bits are 1 at same positon after doing XOR they become 0, so if from
				   #chosen bit we have 1 turned ON on both the bit it means we can create an 
				   #bigger XOR by turning any one of them OFF. by turning one of them off we are
				   #getting smaller number than given number also, which satisfies the given
				   #Condition.we do a&b to check if there is atleast one position in which both
				   #the number has same bit.
				   #		2 -> 10
				   #		2 -> 10
				   #			 - we can change this one so that instead of XOR becoming 0
				   #			   we get bigger XOR value
		print("NO")
	else:
		print("YES")

	

