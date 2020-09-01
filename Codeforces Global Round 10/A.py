"""
1392A - Omkar and Password
https://codeforces.com/contest/1392/problem/A
"""
#Solution Explanation:
"""
If your array consists of one number repeated n times, then you obviously can't do any moves to shorten the password.
Otherwise,you can show that it is always possible to shorten the password to 1 number.

For an array consisting of 2 or more distinct elements, considering the maximum value of the array.
If its max value appears once, you can just repeat operations on the maximum array value until you are left with one number.
What if the maximum elements appears more than once? Well, because there must exist at least 2 distinct numbers,
you can always pick a maximum element adjacent to a different number to perform an operation on.
The array will then have one occurrence of a maximum and you can simply repeat using aforementioned logic.
"""


#Python Code
def oamkarPassword(array):
	array.sort()
	if array[0]==array[-1]:
		return(len(array))
	return(1)
if __name__ == '__main__':
    for _ in range(int(input())):
	    n=input()
	    array=[int(i) for i in input().split()]
	    print(oamkarPassword(array))





