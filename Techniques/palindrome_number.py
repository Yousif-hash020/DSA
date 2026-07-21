def Number(num):
    text = str(num)
    left = 0
    right = len(text)-1

    while left<right:

        if text[left] == text[right]:
            return True
        
        left+= 1
        right-=1
    return None

num = 1221
print(Number(num))



