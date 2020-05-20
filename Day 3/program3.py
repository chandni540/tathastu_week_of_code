def removeDuplicate(str, len(str)): 
    index = 0
    for i in range(0, len(str)):  
        for j in range(0, i + 1): 
            if (str[i] == str[j]): 
                break
        if (j == i): 
            str[index] = str[i] 
            index += 1
              
    return "".join(str[:index]) 
    
str= input("Enter a string") 
print(removeDuplicate(list(str), len(str)))
