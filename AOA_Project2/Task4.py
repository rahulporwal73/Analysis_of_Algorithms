def task4(p, h):
    # get the dimensions of the input matrix
    m, n = len(p), len(p[0])
    
    # initialize variables to store the maximum size and location of the square
    maxRows, maxCols = 1, 1
    maxSize = 2
    
    # initialize dynamic programming tables for rows and columns
    rows_dp = [[0 for j in range(n)] for i in range(m)]
    cols_dp = [[0 for j in range(n)] for i in range(m)]
    
    # calculate the longest consecutive column of each cell in the matrix
    for i in range(m):
        for j in range(n):
            if p[i][j] >= h:
                if i == 0:
                    cols_dp[i][j] = 1
                else:
                    cols_dp[i][j] = cols_dp[i-1][j] + 1
    
    # calculate the longest consecutive row of each cell in the matrix
    for i in range(m):
        for j in range(n):
            if p[i][j] >= h:
                if i - 1 < 0 or j - 1 < 0:
                    rows_dp[i][j] = 1
                else:
                    rows_dp[i][j] = min(rows_dp[i-1][j-1], rows_dp[i-1][j], rows_dp[i][j-1]) + 1
    
    # iterate over each cell in the matrix and calculate the maximum size of a square with that cell as the bottom right corner
    for i in range(2, m):
        for j in range(2, n):
            final_bottomRow = 0
            final_bottomCol = j - 1
            # calculate the length of the longest consecutive column starting from the cell to the left of the current cell
            while(final_bottomCol >= 0 and p[i][final_bottomCol] >= h):
                final_bottomRow += 1
                final_bottomCol -= 1
            # calculate the side length of a square with the current cell as the bottom right corner
            if min(cols_dp[i-1][j], final_bottomRow) < rows_dp[i-1][j-1]:
                side = min(cols_dp[i-1][j], final_bottomRow) + 2
            else:
                final_topRow = 0
                final_topCol = j - 1
                # calculate the length of the longest consecutive row starting from the cell above and to the left of the current cell
                while(i - 1 - rows_dp[i-1][j-1] >= 0 and final_topCol >= 0 and p[i-1-rows_dp[i-1][j-1]][final_topCol] >= h):
                    final_topRow += 1
                    final_topCol -= 1
                # check if a square can be formed with the current cell as the bottom right corner
                if(i - 1 - rows_dp[i-1][j-1] >= 0 and j - 1 - rows_dp[i-1][j-1] >= 0 and final_topRow >= rows_dp[i-1][j-1] and cols_dp[i-1][j-1-rows_dp[i-1][j-1]] >= rows_dp[i-1][j-1]):
                    side = rows_dp[i-1][j-1] + 2
                else:
                    side = rows_dp[i-1][j-1] + 1
    
            # update the maximum size and location of the square if necessary
