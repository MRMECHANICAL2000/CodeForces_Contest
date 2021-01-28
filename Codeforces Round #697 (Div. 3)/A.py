#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

#Library for our use
import math
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
	for _ in range(int(input())):
		n=int(input())
		#Brute
		#Finding all the factor and checking if there is atleast one odd factor - TLE
		"""
		i=2
		if n%2!=0:
			print("YES")
			continue
		while i<=math.sqrt(n):
			if n%i==0:
				if i%2!=0 or (n/i)%2!=0:
					print("YES")
					break
			i+=1
		else:
			print("NO")
		"""

		#Better
		#to say if an number has an odd factor , its just enough to check if it has an odd
		#prime factor. we know any number can be repsented with prime numbers. if there is an
		#prime odd factor then the number has an odd factor. if no prime odd factor means
		#the number does not have an odd divisor. 

		"""
		find the prime factorization of the given number and check if odd exist.
		"""

		#Optimal -shortcut
		#if you watch closely you will know that
		#2 is the only even prime number, if a number does not have odd prime factor it means
		#the number is a power of 2. to check if a number is power of two, wkt all pow 2 
		#no has only one set bit at front.   2->10,4->100,8->1000,16->10000... in binary form

		#   to check if 4 id power of 2 , shortcut : 4&(4-1)

		# 4 -> 100
		# 3 -> 011 &
		#__________
		#	   000 -> if 0 means given no is pow of 2, we print No else Yes

		if n&(n-1):    
			print("YES")
		else:
			print("NO")




"""
# Python3 program to find prime factorization 
# of a number n in O(Log n) time with 
# precomputation allowed. 
import math as mt 

MAXN = pow(10,15)

# stores smallest prime factor for 
# every number 
spf = [0 for i in range(MAXN)] 

# Calculating SPF (Smallest Prime Factor) 
# for every number till MAXN. 
# Time Complexity : O(nloglogn) 
def sieve(): 
	spf[1] = 1
	for i in range(2, MAXN): 
		
		# marking smallest prime factor 
		# for every number to be itself. 
		spf[i] = i 

	# separately marking spf for 
	# every even number as 2 
	for i in range(4, MAXN, 2): 
		spf[i] = 2

	for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
		
		# checking if i is prime 
		if (spf[i] == i): 
			
			# marking SPF for all numbers 
			# divisible by i 
			for j in range(i * i, MAXN, i): 
				
				# marking spf[j] if it is 
				# not previously marked 
				if (spf[j] == j): 
					spf[j] = i 

# A O(log n) function returning prime 
# factorization by dividing by smallest 
# prime factor at every step 
def getFactorization(x): 
	while (x != 1): 
        if x%spf[x]==0:
            print("YES")
            return(True)
		x = x // spf[x] 

	return False

# Driver code 

# precalculating Smallest Prime Factor 
sieve() 
for i in range(int(input())): 
    x =int(input())
    if x%2!=0:
        print("YES")
        continue
    p = getFactorization(x)
    if p:
        print("YES")
    else:
        print("NO")
    # This code is contributed 
# by Mohit kumar 29 

"""


# shortcut for functions
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list



# Region fastio functions

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()