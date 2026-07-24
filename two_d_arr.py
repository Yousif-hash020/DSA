def rows_sum():
    arr = [[1,2], [3,4]]
    max_num = 0

    for i in range(len(arr)):
        rows = 0
        for j in range(len(arr[i])):
            rows += arr[i][j]

        print('rows', i, 'sum', rows)

        if rows > max_num:
            max_num = rows

    return print("max_num is",max_num, "\n")   

rows_sum()


def columns_sum():
    arr = [[1,2],[3,4]]

    max_num = 0

    for col in range(len(arr[0])):
        col1 = 0
        for row in range(len(arr)):
            col1 += arr[col][row]
            
        print("Column sum", col1)
        
        if col1 > max_num:
            max_num = col1

    return print("max_num is",max_num, "\n")  

columns_sum()


def diagonal():
    arr = [[1,2],[3,4]]

    diagonal_sum = 0

    for i in range(len(arr)):
        print("diagonals",arr[i][i])
        diagonal_sum += arr[i][i]
    print('diagonal_sum is ',diagonal_sum,"\n")

diagonal()