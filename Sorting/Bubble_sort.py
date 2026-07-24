def Bubble_sort():
    arr = [5,2,4,1]

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)

Bubble_sort()