n = int(input("\nEnter number of values in a dictionary:"))
dict={}
for i in range(n):
    key = input("Enter the key :")
    dict[key] = int(input("Enter the value : "))
single = dict()
for key in dict:
    if dict[key] not in single.values():
        single[key] = dict[key]

print("After removing duplicate values:", single)
