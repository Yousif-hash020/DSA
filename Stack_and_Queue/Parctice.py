def balance(s):
    stack =[]

    for ch in s:
        if ch == "(":
            stack.append(ch)
            
        
        elif ch == ")":
             if not stack:
                 return False
             stack.pop()
            
    print(s)

    return len(stack) == 0 
         
        
print(balance('(()'))

