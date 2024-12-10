def pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:

            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

num_rows = 5
pascals_triangle = pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)