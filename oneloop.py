def One_loop():
    arr = [[1,2],[3,4]]

    for col in range(len(arr[0])):
        row_sum = 0
        column_sum = 0
        diagonal = arr[col][col]

        for row in range(len(arr)):
            row_sum += arr[col][row]
            column_sum += arr[row][col]
            
        print("Row", col, "sum:", row_sum)
        print("Column", col, "sum:", column_sum)
        print("Diagonal value:", diagonal)
        print()

        if row_sum > column_sum:
            print("the greater sum is :", row_sum)
        else:
            print("the greater sum is :", column_sum)
            print()
        
One_loop()