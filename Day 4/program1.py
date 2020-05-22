n = int(input("Enter the number of elements in a tuple: "))
num = []
print("\nElements in the tuple are : ")
for i in range(n):
    num.append(input())
num = tuple(num)
fin = input("Enter the element whose number of occurences is to be found: ")
print("Number of occurences of",fin,"in the tuple is:", a.count(fin))
