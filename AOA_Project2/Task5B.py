def task5B(matrix, h):
    # Get the dimensions of the input matrix
    m, n = len(matrix), len(matrix[0])
    
    # If the matrix is a single row or a single column, the answer is (1,1,1,1)
    if m==1 or n==1:
        print(1, 1, 1, 1)
        exit()
    
    # Initialize variables to keep track of the maximum sub-matrix
    max_row, max_col = 0, 0
    maxlen=0
    
    # Initialize the dynamic programming matrix M
    M = [[0]*n for _ in range(m)]
    
    # Set the values of the first row and first column of M to 2
    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                M[i][j]=2
    
    # Fill in the rest of M using dynamic programming
    for i in range(1,m-1):
        for j in range(1,n-1):
            # If the current element of the input matrix is less than h, set M[i][j] to 2
            if matrix[i][j] < h:
                M[i][j]=2
            # If all 8 neighboring elements are greater than or equal to h, update M[i][j] accordingly
            elif matrix[i-1][j-1]>=h and matrix[i-1][j+1]>=h and matrix[i+1][j-1]>=h and matrix[i+1][j+1]>=h and matrix[i-1][j]>=h and matrix[i][j-1]>=h and matrix[i+1][j]>=h and matrix[i][j+1]>=h:
                M[i][j] = min(M[i-1][j-1],M[i-1][j],M[i][j-1]) + 1
            # If any of the neighboring elements are less than h, set M[i][j] to 2
            elif matrix[i-1][j]<h or matrix[i][j-1]<h or matrix[i+1][j]<h or matrix[i][j+1]<h:
                M[i][j] = 2
            # Otherwise, set M[i][j] to 3
            else:
                M[i][j] = 3
            
            # Update maxlen and the position of the maximum sub-matrix if M[i][j] is greater than or equal to maxlen
            if M[i][j] >= maxlen:
                maxlen = M[i][j]
                max_row = i+1
                max_col=j+1
    
    # Print the answer
    print (max_row-maxlen + 2, max_col-maxlen + 2, max_row + 1, max_col + 1)

# Get input from the user and call the task5B function
m, n, h = input().split()
m, n, h = int(m), int(n), int(h)
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
task5B(matrix, h)
