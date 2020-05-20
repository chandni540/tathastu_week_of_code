n1 = int(input("Enter number of elements in list 1: "))
print("Enter the elements in a list 1 : ")
list1 = []
for i in range(n1):
    list1.append(input())
n2 = int(input("Enter number of elements in list 2: "))
print("Enter the elements in a list 2 : ")
list2 = []
for i in range(n2):
    list1.append(input())
list3 = []
for x in list1:
    list3.append(x)
for x in list2:
    list3.append(x)

print("The intersection of list 1 and list 2 is : ",list3)
