import math
for _ in range(int(input())):
	n=int(input())
	string=input()
	if string==string[::-1]:
		count_zero=string.count("0")
		alice=0
		bob=0
		if count_zero==1:
			print("BOB")
			continue

		if count_zero%2!=0:
			print("ALICE")
		else:
			print("BOB")
	else:
		palinZero=0
		nonPalinZero=0
		for i in range(len(string)):
			if string[i]=='0':
				if string[n-1-i]=='0':
					palinZero+=1
				else:
					nonPalinZero+=1

		if (nonPalinZero==1 and string[(n//2)]=='0' and palinZero+nonPalinZero==2):
			print("DRAW")
		else:
			print("ALICE")