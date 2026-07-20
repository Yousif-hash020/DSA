def rev_arr():
    arr = [10,20,30,40,50]
    item = arr.pop()
    arr.insert(0,item)

    print(arr)
rev_arr()