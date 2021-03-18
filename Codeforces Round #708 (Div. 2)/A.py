from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    hashTable=defaultdict(int)
    for i in array:
        hashTable[i]+=1
    ans=sorted(hashTable.keys())
    for i in hashTable:
        if hashTable[i]>1:
            ans.extend([i for x in range(hashTable[i]-1)])
    print(*ans)