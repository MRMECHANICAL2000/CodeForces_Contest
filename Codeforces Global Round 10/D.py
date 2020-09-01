from math import ceil
def main():
	for _ in range(int(input())):
		size=int(input())
		array=list(input())
		ans=0

		count=0
		while len(array) and array[0]==array[-1]:
			count+=1
			array.pop()
		if len(array)==0:
			if count<=2:
				print(0)
			else:
				print((count+2)//3)
			continue
		array.append("$")
		for i in range(len(array)-1):
			count+=1
			if array[i]!=array[i+1]:
				ans+=count//3
				count=0
		print(ans)


if __name__ == '__main__':
	main()