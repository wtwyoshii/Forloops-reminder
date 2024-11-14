def column_sums(matrix):
    num_cols = len(matrix[0])

    for col in range(num_cols):
        column_sum = 0
        for row in matrix:
            column_sum += row[col]
        print(f"Column {col + 1}: {column_sum}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column_sums(matrix)