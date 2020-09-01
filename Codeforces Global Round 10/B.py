"""
1392B - Omkar and Infinity Clock
https://codeforces.com/contest/1392/problem/B

#Solution Explanation
There's only two possible states the array can end up as. 
Which state it becomes after k turns is determined solely by the parity of k.
After the first move, the array will consists of all non-negative numbers (d−ai will never be negative because ai never exceeds d). 
After one turn, let's define x as max(ai) over all i. For any number ai, it will turn into x−ai. Because a zero will always exist after any one operation, x will be the maximum of the array in the next turn as well.
Then the value at index i will turn into x−(x−ai). This is just equal to ai!
Now that it's obvious that our array will enter a cycle with a period of 2,
we simply do the following: If k is odd, perform 1 operation. Otherwise perform 2 operations.
"""
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	array=[int(i) for i in input().split()]
	
	for j in range(2 if k%2==0 else 3):
		d=max(array)
		array=[d-i for i in array] 
	print(*array)




