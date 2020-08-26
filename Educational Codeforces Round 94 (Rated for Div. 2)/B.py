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
		myCapacity,friendCapcity=Ilist()
		countSword,countWarAxe=Ilist()
		SwordWeight,WarAxeWeight=Ilist()
		if SwordWeight>WarAxeWeight:
			SwordWeight,WarAxeWeight=WarAxeWeight,SwordWeight
			countSword,countWarAxe=countWarAxe,countSword
		TotalCount=myCapacity//SwordWeight+friendCapcity//SwordWeight
		if TotalCount<=countSword:
			print(TotalCount)
			continue
		else:
			TotalCount=countSword
			for i in range(0,countSword+1):
				p,f=myCapacity,friendCapcity
				p-=SwordWeight*i
				f-=(countSword-i)*SwordWeight
				if p>=0 and f>=0:
					TotalCount=max(TotalCount,countSword+p//WarAxeWeight+f//WarAxeWeight)
		print (min(TotalCount,countSword+countWarAxe)) 
	
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list

if __name__ == '__main__':
    main()