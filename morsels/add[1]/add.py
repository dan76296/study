def add(*args):
    results = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j]+matrix2[i][j])
        results.append(row)
    return results
