def count():
    arr = [1,2,3,3,2,1,4,4,3]

    seen = set()

    for i in arr:
        if i not in seen:
         count = arr.count(i)
         if count > 1:
          print(i,'item', 'repeated', count)
        seen.add(i)
count()