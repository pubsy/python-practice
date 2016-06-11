A = [[1,2,3],[3,4,5],[6,7,8]]
B = [[1,1,1],[2,2,2],[3,3,3]]
C = [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(A)):
    for j in range(len(A)):
        sum = 0
        for k in range(len(A)):
            sum += A[i][k] * B[k][j]
        C[i][j] = sum

for i in range(len(C)):
    print('\n')
    for j in range(len(C)):
        print(str(C[i][j]) + ',')