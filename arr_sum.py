def arr():
    arr = [1,2,3,4]

    total = sum(arr)

    for i in range(len(arr)):
        arr[i] = total - arr[i]
        
    print(arr)

arr()