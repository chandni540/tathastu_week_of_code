def sort(li):
    oddlist = []
    evenlist = []
    for i in li:
        if i%2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    return sorted(odd, reverse = True) + sorted(even)

n = int(input("Enter the size of the list : "))
li = []
for i in range(n):
    li.append(int(input("Enter element "+str(i+1)+" : ")))
print("The sorted list is as follows : ",sort(li))
