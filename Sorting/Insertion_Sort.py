def Insertion_Sort():
    arr = [5,3,4,2,1]

    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1

        arr[j+1] = key
        
    print(arr)

Insertion_Sort()