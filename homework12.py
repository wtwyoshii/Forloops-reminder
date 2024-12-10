maze = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]
def find_path(maze):
    rows = len(maze)
    cols = len(maze[0])
    path = []

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                path.append((i, j))

    for coordinate in path:
        print(coordinate)

find_path(maze)
