def bounding_indices(matrix, h, K):
    m, n = len(matrix), len(matrix[0])
    min_row, min_col = m+1, n+1
    maxlen=0
    row_k_count=[[0]*n for _ in range(m)]   # precompute cumulative k values rowwise and columnwise
    col_k_count=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < h:
                if j==0:
                    row_k_count[i][j]=1
                else:
                    row_k_count[i][j]=row_k_count[i][j-1]+1
            else:
                if j==0:
                    row_k_count[i][j]=0
                else:
                    row_k_count[i][j]=row_k_count[i][j-1]
    for j in range(n):
        for i in range(m):
            if matrix[i][j]<h:
                if i==0:
                    col_k_count[i][j]=1
                else:
                    col_k_count[i][j]=col_k_count[i-1][j]+1
            else:
                if i==0:
                    col_k_count[i][j]=0
                else:
                    col_k_count[i][j]=col_k_count[i-1][j]
                
    M = [[[None for k in range(K+1)] for j in range(n)] for i in range(m)] #DP array 3D
    
    def dp(i, j, k):
        nonlocal maxlen, min_row, min_col
        
        if M[i][j][k] is not None: #if M already computed
            return M[i][j][k]
        
        if k == 0:              #base case of bellman equation
            if (i==m-1 or j==n-1):
                if matrix[i][j] < h:
                    M[i][j][k]=0
                else:
                    M[i][j][k]=1
            else:
                M[i][j][k]=0
        
        else:
            if (i==m-1 or j==n-1):
                M[i][j][k]=1
            
            else:       #bellman equation cases
                if matrix[i][j] < h:
                    max_potential_size = dp(i+1, j+1, k)
                    for z in range(max_potential_size,-1,-1):
                        r = row_k_count[i][j+z] - row_k_count[i][j]
                        c = col_k_count[i+z][j] - col_k_count[i][j]
                        if (r+c+1) <= k:
                            subproblem = dp(i+1, j+1, k-(r+c+1))
                            M[i][j][k] = min(subproblem,z)+1
                            break
                else:
                    max_potential_size = dp(i+1, j+1, k)
                    for z in range(max_potential_size,-1,-1):
                        r = row_k_count[i][j+z] - row_k_count[i][j]
                        c = col_k_count[i+z][j] - col_k_count[i][j]
                        if (r+c) <= k:
                            subproblem = dp(i+1, j+1, k-(r+c))
                            M[i][j][k] = min(subproblem,z)+1
                            break
                
        if M[i][j][k] >= maxlen: #updating max square area values and indices
            maxlen = M[i][j][k]
            min_row=i
            min_col=j
        
        return M[i][j][k]
    
    dp(0, 0, K)
    print(min_row+1,min_col+1,min_row+maxlen,min_col+maxlen)
    
m, n, h, k = input().split()
m, n, h, k = int(m), int(n), int(h), int(k)
p = []

for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

bounding_indices(p, h,k)
