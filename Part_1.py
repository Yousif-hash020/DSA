def count_even(number):
    count = 0
    
    for i in range(1, number+1):
       
        if i % 2 == 0:
            count = count+1
    return count    
     
        
user_input = input('enter a num')
user_input = int(user_input)

result = count_even(user_input)

print (result)