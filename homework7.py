list = [[1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
]
rows = len(list)
cols = len(list[0])

transpose = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = list[i][j]

is_symmetric = True
if rows == cols:
    for i in range(rows):
        for j in range(cols):
            if list[i][j] != transpose[i][j]:
                is_symmetric = False
                break
else:
    is_symmetric = False
print("Original List:")
for row in list:
    print(row)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)

if is_symmetric:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")