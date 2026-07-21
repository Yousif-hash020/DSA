def addtwo(n1,n2):
    if n2 == 0 :
        return n1
    return addtwo(n1+1, n2-1)

print(addtwo(1,2))