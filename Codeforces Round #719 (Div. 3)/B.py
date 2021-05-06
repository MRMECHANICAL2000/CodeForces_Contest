for _ in range(int(input())):
	n=input()
	if int(n)<=9:
		print(n)
	else:
		ans=(len(n)-1)*9
		if int(n[1:])>=int(n[0])*int('1'*(len(n)-1)):
			ans+=int(n[0])
		else:
			ans+=int(n[0])-1
		print(ans)


