n = int(input("Enter size of array: "))
li = []
for i in range(n):
    li.append(int(input("Enter the elements : ")))

position = 1
for i in li:
    if i==position:
        position+=1
        
print("Smallest positive number absent in the list :", position)
