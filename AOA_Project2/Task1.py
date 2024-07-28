def task1(matrix, h):
    m, n = len(matrix), len(matrix[0])  #matrix represents p[][] matrix
    final_minrow, final_mincol, final_maxrow, final_maxcol = 0, 0, 0, 0
    for i in range(m):
        for j in range(n):
            if(matrix[i][j] >= h):   #only going to check for square if the value is >=h
                max_row = i
                max_col = j
                while (max_row < m and max_col < n):  #will compute all possible square areas from i,j 
                    isSquare = True                     #flag to check if any plot in the square is <h
                    for k in range(i,max_row + 1):
                        for l in range(j, max_col + 1):
                            if matrix[k][l] >= h:
                                continue
                            else:
                                isSquare = False  #flag set to false if any plot in the square area has <h trees

                    if isSquare and (final_maxrow - final_minrow) < (max_row - i): #storing value of maximum square area and the topleft and bottom right plot indices
                        final_minrow = i + 1    
                        final_mincol = j + 1
                        final_maxrow = max_row + 1
                        final_maxcol = max_col + 1

                    max_row+=1
                    max_col+=1
    print(final_minrow, final_mincol, final_maxrow, final_maxcol) #output

m, n, h = input().split()         #reading input
m, n, h = int(m), int(n), int(h)
p = []

for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

task1(p, h)




