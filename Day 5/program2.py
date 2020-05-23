n = int(input("Enter the size of the list : "))
li = []
for i in range(n):
    li.append(int(input()))

for i in range(n-1):
    li[i] = max(li[i+1:])
    
print("\nUpdated list is : ", li)
