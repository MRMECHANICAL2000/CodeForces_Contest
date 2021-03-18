from collections import defaultdict
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    array=list(map(int,input().split()))
    hashTable=defaultdict(int)
    mDivisible=[]
    for i in array:
        if i%m==0:
            mDivisible.append(i)
        else:
            hashTable[i%m]+=1


    count=0
    #print(hashTable)
    for i in hashTable.keys():
        if hashTable[i]:
            if abs(m-i)==i:
                count+=1
                hashTable[i]=0
            elif abs(m-i) in hashTable and hashTable[abs(m-i)]:
                count+=1
                minAmount=min(hashTable[i],hashTable[abs(m-i)])
                if hashTable[i]==minAmount:
                    hashTable[i]=0
                else:
                    hashTable[i]-=minAmount+1

                if hashTable[abs(m-i)]==minAmount:
                    hashTable[abs(m-i)]=0
                else:
                    hashTable[abs(m-i)]-=(minAmount+1)
    #print(mDivisible,hashTable,count)
    count+=sum(hashTable.values())+ (1 if mDivisible else 0)
    print(count)

