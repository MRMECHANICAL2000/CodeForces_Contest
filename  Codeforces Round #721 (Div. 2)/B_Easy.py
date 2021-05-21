import math
for _ in range(int(input())):
	n=int(input())
	string=input()
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