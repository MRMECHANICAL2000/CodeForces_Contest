from collections import Counter
for _ in range(int(input())):
	string=input()
	hashTable=Counter(string)
	if len(hashTable)==1 and string=="a"*len(string):
		print("NO")
	else:
		print("YES")
		if "a"+string!=string[::-1]+"a":
			print("a"+string)
		else:
			print(string+"a")


