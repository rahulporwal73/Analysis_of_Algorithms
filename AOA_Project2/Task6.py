# define a function named 'task6' that takes three arguments:
# a matrix, an integer 'h', and another integer 'k2'
def task6(matrix, h, k2):
    # get the number of rows and columns of the matrix
    m, n = len(matrix), len(matrix[0])
    
    # initialize variables to keep track of the coordinates of the largest square
    final_minrow, final_mincol, final_maxrow, final_maxcol = 0, 0, 0, 0
    
    # loop through all possible starting points for a square in the matrix
    for i in range(m):
        for j in range(n):
            # initialize variables to keep track of the current maximum row and column
            max_row = i
            max_col = j
            
            # loop through all possible square sizes starting from the current point
            while (max_row < m and max_col < n):
                # initialize variables for checking whether the current square satisfies the conditions
                isSquare = True
                counter = 0
                
                # loop through all elements in the current square
                for k in range(i, max_row + 1):
                    for l in range(j, max_col + 1):
                        # if the element is greater than or equal to 'h', move on to the next one
                        if matrix[k][l] >= h:
                            continue
                        # if the element is less than 'h', increment the 'counter'
                        else:
                            counter += 1
                            # if the 'counter' exceeds 'k2', the square does not satisfy the conditions
                            if counter > k2:
                                isSquare = False
                            else:
                                continue
                                
                # if the current square satisfies the conditions and is larger than the current largest square, update the variables
                if isSquare and (final_maxrow - final_minrow) <= (max_row - i):
                    final_minrow = i + 1
                    final_mincol = j + 1
                    final_maxrow = max_row + 1
                    final_maxcol = max_col + 1
                    
                # increment the maximum row and column to check the next larger square
                max_row+=1
                max_col+=1
    
    # print the coordinates of the largest square that satisfies the conditions
    print(final_minrow, final_mincol, final_maxrow, final_maxcol)
    
# read the inputs from the user
m, n, h, k = input().split()
m, n, h, k = int(m), int(n), int(h), int(k)
p = []

# read the matrix from the user
for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

# call the 'task6' function with the inputs
task6(p, h, k)
