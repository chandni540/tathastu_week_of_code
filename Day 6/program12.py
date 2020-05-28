n = int(input("Enter number of strings: "))
li = []
for i in range(n):
     li.append(str(input("Enter string : ",i+1)))   
li.sort()
print('\nThe list is  : ',li)
n1,n2 = len(li[0]), len(li[n-1]) 
res = "" 
      
i,j = 0,0
while(i <= n1 - 1 and j <= n2 - 1): 
    if (li[0][i] != li[n-1][j]): 
        break
    res += (li[0][i]) 
    i += 1
    j += 1

print("Longest common prefix:", res)
