n = int(input("Enter size of list: "))
li = []
for i in range(n):
     li.append(int(input("Enter the elements : "))) 
li.sort(reverse = True)

print("\nLargest product of 3 nummbers in list is:", li[0]*li[1]*li[2])
