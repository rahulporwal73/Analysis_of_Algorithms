def task2(p, h):
    # Get the number of rows and columns in the 2D list
    m = len(p)
    n = len(p[0])
    
    # Initialize variables to track the minimum row and column indices
    # and the maximum side length of a square with height h
    maxside = 0
    minrow = m+1
    mincol = n+1
    
    # Iterate through each plot in the 2D list
    for i in range(m):
        for j in range(n):
            # If the height of the current plot is greater than or equal to h,
            # then check if there is a square with height h that includes this plot
            if p[i][j]>=h:
                # Initialize a flag and a side length to track whether a square is found
                flag=True
                side=1
                
                # Keep checking squares with increasing side lengths until a square 
                # with height h cannot be formed or the end of the 2D list is reached
                while (i+side < m and j+side < n and flag):
                    x=j
                    while x<=side+j:
                        if p[i+side][x] < h:
                            flag=False
                            break
                        x+=1
                    y=i
                    while y<=side+i:
                        if p[y][j+side] < h:
                            flag=False
                            break
                        y+=1
                    if flag:
                        side+=1
                
                # If a square with height h was found and its side length is greater than
                # the previous maximum side length, update the minimum row and column indices
                # and the maximum side length
                if maxside < side:
                    maxside = side
                    minrow = i
                    mincol = j
    
    # Output the minimum row and column indices of the bottom left corner of the largest
    # square with height h and its top left corner indices
    print(minrow+1,mincol+1,minrow+maxside,mincol+maxside)

# Get the input values for m, n, h and create the 2D list p
m, n, h = input().split()
m, n, h = int(m), int(n), int(h)
p = []
for i in range(m):
    row = list(map(int, input().split()))
    p.append(row)

# Call the task2 function with the 2D list p and height h as input
task2(p, h)
