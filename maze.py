table = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == 3:
            print(f"3 found at position: ({i}, {j})")