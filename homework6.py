numbers = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]
]

num_columns = len(numbers[0])

for col in range(num_columns):
    column_sum = 0

    for row in numbers:
        column_sum += row[col]
    print(f"Sum of column {col}: {column_sum}")