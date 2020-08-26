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
	for i in range(Iint()):
		n,k=Ilist()
		if n<k:
			print(k-n)
		elif (n%2==k%2):
			print(0)
		else:
			print(1)
	
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list

if __name__ == '__main__':
    main()