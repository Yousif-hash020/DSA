def Quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for element in arr[:-1]:

        if element < pivot:
            left.append(element)

        else:
            right.append(element)


    return Quick_sort(left) + [pivot] + Quick_sort(right)

arr = [5, 2, 8, 1, 4]

print(Quick_sort(arr))
