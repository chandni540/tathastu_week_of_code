def Permutation(string,start,end):  
    current = 0;   
    if(start == end):  
        print(string);  
    else:   
        for current in range(start,end+1):  
            li = list(string)  
            temp = li[start]
            li[start] = li[current]  
            li[current] = temp
              

            Permutation("".join(li),start+1,end)  
            temp = li[start]  
            li[start] = li[current] 
            li[current] = temp 
  
str = input("Enter the string : ")   
Permutation(str,0,len(str)-1)  
