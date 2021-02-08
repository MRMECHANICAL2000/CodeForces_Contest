for _ in range(int(input())):
	string=input()
	ans=""
	for idx,val in enumerate(string):
		if idx%2==0:
			if val!="a":
				ans+="a"
			else:
				ans+="b"
		else:
			if val!="z":
				ans+="z"
			else:
				ans+="y"
	print(ans)



