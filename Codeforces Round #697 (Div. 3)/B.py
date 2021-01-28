import math
for _ in range(int(input())):
	n=int(input())

	if n%2020==0:
		print("YES")
		continue
	elif n%2021==0:
		print("YES")
		continue
	rem=n%2020
	quo=n//2020

	if rem<=quo:
		print("YES")
		continue
	print("NO")