X = int(input())  

count = 0  
stick_length = 64  

while X > 0: 
    if stick_length > X:  
        stick_length //= 2  
    else:  
        X -= stick_length  
        count += 1 
        stick_length //= 2  

print(count)  
