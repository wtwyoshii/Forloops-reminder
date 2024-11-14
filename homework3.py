def rotate_grid(grid):
    n = len(grid)
    rotated = [[0] * n for _ in range(n)]  # Initialize an empty rotated grid
    
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = grid[i][j]  # Rotate clockwise by 90 degrees
            
    for row in rotated:
        print(row)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_grid(grid)