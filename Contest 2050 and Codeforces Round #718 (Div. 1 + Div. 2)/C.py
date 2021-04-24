def valuePlacer(i,j,val,count):
	if count:
		if j-1>=0 and matrix[i][j-1]==0:
			matrix[i][j-1]=val
			count-=1
			valuePlacer(i,j-1,val,count)

		elif i+1<n and matrix[i+1][j]==0:
			matrix[i+1][j]=val
			count-=1
			valuePlacer(i+1,j,val,count)

n=(int(input()))
matrix=[[0 for j in range(n)] for i in range(n)]
val=list(map(int,input().split()))
for i in range(n):
	matrix[i][i]=val[i]

for i in range(n):
	valuePlacer(i,i,matrix[i][i],matrix[i][i]-1)
for i in matrix:
	for j in i:
		if j==0:
			break
		print(j,end=" ")
	print()

