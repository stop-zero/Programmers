word = input()  
count = [0] * 26  

for char in word:
    index = ord(char) - ord('a') 
    count[index] += 1

result = ' '.join(map(str, count))  
print(result)
