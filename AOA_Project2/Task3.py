def task3(matrix, h):
    m, n = len(matrix), len(matrix[0])
    M = [[0]*n for _ in range(m)]   #DP array of size mxn to store side of max square with (i,j) as bottom right plot 
    max_len = 0                     #max_len will keep track of the maximum square area found till (i,j) 
    max_i, max_j = 0, 0             #max_i, max_j store bottom right indices of max square found
    for i in range(m):
        for j in range(n):
            if matrix[i][j] >= h:
                if i == 0 or j == 0:        #base case
                    M[i][j] = 1
                else:
                    M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1]) + 1 #bellman equation
                if M[i][j] > max_len:       #updating max square found upto (i,j)
                    max_len = M[i][j]
                    max_i, max_j = i, j
    print (max_i-max_len + 2, max_j-max_len + 2, max_i + 1, max_j + 1)


m, n, h = input().split()
m, n, h = int(m), int(n), int(h)
p = []

for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

task3(p, h)