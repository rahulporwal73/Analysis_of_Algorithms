def task5A(matrix, h):
    m, n = len(matrix), len(matrix[0])
    if m==1 or n==1:  # if matrix has only one plot or all plots stored in a single row or column
        print(1, 1, 1, 1)
        exit()
    M = [[0]*n for _ in range(m)]  
    #DP array of size mxn
    # M[i][j] will have side of max square area possible using (i+1,j+1) as bottom right plot
    def mcompute(i,j): #recursive function
        if(M[i][j] != 0):
            return M[i][j]  #if M[i][j] is already available, do not recompute
        if i==0 or j==0:   #bellman equation
            M[i][j]=2       
        elif p[i-1][j-1]>=h and p[i-1][j+1]>=h and p[i+1][j-1]>=h and p[i+1][j+1]>=h and p[i-1][j]>=h and p[i][j-1]>=h and p[i+1][j]>=h and p[i][j+1]>=h and p[i][j]>=h:
            M[i][j] = min(mcompute(i-1,j-1),mcompute(i-1,j),mcompute(i,j-1))+1
        elif p[i-1][j]<h or p[i][j-1]<h or p[i+1][j]<h or p[i][j+1]<h or p[i][j]<h:
            M[i][j]=min(1, mcompute(i-1,j-1),mcompute(i-1,j),mcompute(i,j-1))+1
        else:
            M[i][j]=min(2, mcompute(i-1,j-1),mcompute(i-1,j),mcompute(i,j-1))+1
        return M[i][j]
    mcompute(m-2,n-2) #recursive function call 
    maxlen = max(max(M)) #traceback M[][] to get indices of the topleft and bottom right plots of the max square area
    for i in range(m):
        for j in range(n):
            if M[i][j] == maxlen:
                maxrow = i+1
                maxcol = j+1
                break
    print (maxrow-maxlen + 2, maxcol-maxlen + 2, maxrow + 1, maxcol + 1)

m, n, h = input().split()
m, n, h = int(m), int(n), int(h)
p = []

for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

task5A(p, h)