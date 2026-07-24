def Optimize():
    arr = [5,2,4,1,6,3]

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)

Optimize()