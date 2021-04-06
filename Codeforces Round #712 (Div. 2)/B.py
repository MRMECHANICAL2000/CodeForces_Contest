
for _ in range(int(input())):
	n=int(input())
	string=input()
	req=input()
	array=[]
	one=0
	zero=0
	for i in string:
		if i=="0":
			zero+=1
		else:
			one+=1
		if one==zero:
			array.append(True)
		else:
			array.append(False)
	invert=0
	#print(one,zero,array)

	for i in range(n-1,-1,-1):
		if not invert and req[i]==string[i]:
			pass
		elif not invert and req[i]!=string[i]:
			if array[i]: 
				invert=1
			else:
				print("NO")
				break

		elif invert and req[i]!=str(1-int(string[i])):
			if not array[i]:
				print("NO")
				break
			invert=0


	else:
		print("YES")
