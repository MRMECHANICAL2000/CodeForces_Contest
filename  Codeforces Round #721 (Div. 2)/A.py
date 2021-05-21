for _ in range(int(input())):
	n=int(input())
	if n==1:
		print(0)
		continue
	binRep=bin(n)[2:]
	print(int('1'*(len(binRep)-1),2))

