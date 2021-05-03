for _ in range(int(input())):
	n,x=list(map(int,input().split()))
	array=list(map(int,input().split()))
	array.sort(reverse=True)
	sumVal=0

	if sum(array)==x:
		print("NO")
	elif sum(array)<x:
		print("YES")
		print(*array)

	else:

		temp=[]
		accepted=[]
		for idx,val in enumerate(array):
			sumVal+=val
			accepted.append(val)
			if sumVal==x:
				sumVal-=val
				if idx!=len(array)-1 and array[idx+1]!=array[idx]:
					accepted.pop()
					accepted.append(array[idx+1])
					accepted.append(array[idx])
					print("YES")
					print(*accepted,*array[idx+2:],*temp)
					break				

				temp.append(accepted.pop())
			elif sumVal>x:
				print("YES")
				print(*accepted,*array[idx+1:],*temp,)
				break
		else:
			print("NO")
		#print(accepted,temp)

