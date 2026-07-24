def Sum():
    array = [1,2,3,4]

    total = sum(array)

    for i in range(len(array)):

        array[i] = total - array[i]
    print(array)

Sum()
