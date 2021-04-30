n=int(input())
array1=[i+0.0 for i in list(map(int,input().split()))]
array2=[i+0.0 for i in list(map(int,input().split()))]
totalSum=sum([array2[i]*array1[i] for i in range(n)])+0.0
maxSum=totalSum

for i in range(n):
    for j in range(i,i+2):
        start=i
        end=j
        curSum=totalSum
        while start>=0 and end<n:
            curSum=curSum-array1[start]*array2[start]-array1[end]*array2[end]
            curSum=curSum+array1[start]*array2[end]+array1[end]*array2[start]
            #curSum+=(array1[start]-array1[end])*(array2[end]-array2[start])

            start-=1
            end+=1
            maxSum=max(maxSum,curSum)
print(int(maxSum))
"""

for i in range(n):
    #for j in range(i,i+2):
    start=i
    end=i
    curSum=totalSum
    while start>=0 and end<n:
        curSum+=(array1[start]-array1[end])*(array2[end]-array2[start])
        start-=1
        end+=1
        maxSum=max(maxSum,curSum)

for i in range(n):
    start=i
    end=i+1
    curSum=totalSum
    while start>=0 and end<n:
        curSum+=(array1[start]-array1[end])*(array2[end]-array2[start])
        start-=1
        end+=1
        maxSum=max(maxSum,curSum)

print(maxSum)

"""

