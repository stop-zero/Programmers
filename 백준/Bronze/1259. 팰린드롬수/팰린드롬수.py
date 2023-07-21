while True:
    number = input()
    
    if number == '0':
        break
    
    result = 'no'
    
    if number == number[::-1]:
        result ='yes'
        
    print(result)