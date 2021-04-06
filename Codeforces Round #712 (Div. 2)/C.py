for _ in range(int(input())):
	n=int(input())
	string=input()
	a=""
	b=""
	oneCount=string.count("1")
	zeroCount=string.count("0")
	if string[0]==string[-1]=="1":
		if oneCount%2==0 and zeroCount%2==0:
			one=0
			zero=0
			for i in string:
				if i=="1":
					one+=1
					if oneCount//2>=one:
						a+="("
						b+="("
					else:
						a+=")"
						b+=")"
				elif i=="0":
					zero+=1
					if zero%2==0:
						a+="("
						b+=")"
					else:
						a+=")"
						b+="("
			print("YES")
			print(a)
			print(b)

		else:
			print("NO")
	else:
		print("NO")

