#For binary search problem try comparing the mid
#with next value always. so that your ans will remain
#in the left pointer and return it at last.

import sys
import math
n=int(input())
l=1
r=n
while l<r:
	m=l+math.ceil((r-l)/2) #Dont forget to ceil or you will end up in self loops
						   #if you are finding mid of 7,8 you will always
						   #end up picking 7th index and if your ans is in 8 you will either
						   #get wrong answer or end up in self loops.
						   #so always go with val,nextVal comparison or with val and math.ceil()
						   #while finding middle element
	print("?",m,flush=True)
	val=int(input())
	print("?",m-1,flush=True)
	prevVal=int(input())
 
	if prevVal>val:
		l=m
	else:
		r=m-1
 
print('!',l,flush=True)