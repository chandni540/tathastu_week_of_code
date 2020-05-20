n = int(input("Enter number of elements: "))
print("Enter the elements in a list : ")
list1 = []
list2 =[]
for i in range(n):
    list1.append(input())
for x in list1:
    if x not in list2:
        list2.append(x)

print("List without duplicacy :", list2)
