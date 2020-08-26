


# import math
# from collections import Counter
# from collections import defaultdict
# from collections import deque
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import accumulate,permutations as perm,combinations as comb
# import heapq
# from functools import reduce
# from fractions import Fraction
# import sys

def main():
	for _ in range(Iint()):
		s=list(map(int,input()))
		x=Iint()
		n=len(s)
		w=[1 for i in s]
		for i in range(n):
			if s[i]==0:
				if i>=x:
					w[i-x]=0
				if i+x<len(s):
					w[i+x]=0
		newString=[]
		for i in range(n):
			temp=0
			if i>=x and w[i-x]==1:
				temp=1
			if i+x<len(s) and w[i+x]==1:
				temp=1
			newString.append(temp)
			#print(n,s,newString)
		if newString==s:
			Plist(w)
		else:
			print(-1)



	
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=''): print(s.join(map(str, li)))   # non string list

if __name__ == '__main__':
    main()