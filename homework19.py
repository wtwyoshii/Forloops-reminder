def common_sequence(list1, list2):
    lcs_matrix = [[0] * (len(list2) + 1) for _ in range(len(list1) + 1)]

    for i in range(1, len(list1) + 1):
        for j in range(1, len(list2) + 1):
            if list1[i - 1] == list2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
    
    lcs = []
    i, j = len(list1), len(list2)
    while i > 0 and j > 0:
        if list[i-1] == list2[j-1]:
            lcs.append(list1[i-1])
            i -= 1
            j -= 1
        elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs[::-1]

list1 = [1, 2, 3, 4, 5]
list2 = {2, 3, 4, 6, 7}
result = common_sequence(list1, list2)
print(result)