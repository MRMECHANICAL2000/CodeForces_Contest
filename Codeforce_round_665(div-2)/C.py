#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

# import math
from collections import Counter
# from collections import defaultdict
# from collections import deque
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import accumulate,permutations as perm,combinations as comb
# import heapq
# from functools import reduce
# from fractions import Fraction
# import sys
from math import gcd
def main():
	for _ in range(Iint()):
		Iint()
		array=Ilist()
		minVal=min(array)
		newArr=[]
		keyArray=[]
		valArray=[]

		for i,v in enumerate(array):
			if v%minVal==0:
				newArr.append([i,v])
				keyArray.append(i)
				valArray.append(v)
		valArray.sort()

		for i,v in enumerate(keyArray):
			array[v]=valArray[i]
		"""

		#print(array,newArr)

		for i in range(len(newArr)-1):
			LocalMinVal=newArr[i][1]
			LocalMinIndex=i
			for j in range(i,len(newArr)):
				if LocalMinVal>newArr[j][1]:
					LocalMinVal=newArr[j][1]
					LocalMinIndex=j
			else:
				newArr[i][1],newArr[LocalMinIndex][1]=newArr[LocalMinIndex][1],newArr[i][1]
				array[newArr[i][0]],array[newArr[LocalMinIndex][0]]=array[newArr[LocalMinIndex][0]],array[newArr[i][0]]
				#newArr[i][0],newArr[j][0]=newArr[j][0],newArr[i][0]
		"""

					

			#print(newArr)
		#print(array,minVal,newArr)
		if array==sorted(array): 
			print("YES")
		else:
			print("NO")
		

			

	
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