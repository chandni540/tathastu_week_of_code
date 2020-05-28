n = int(input("\nEnter size of your list:"))
li=[]
for i in range(n):
    list.append(int(input("Enter element :",i+1)))
print("\nThe list is:",list)

k= int(input("\nEnter the value of k:"))
sort = sorted(li)
print("\nThe kth smallest value in list is=",sort[k-1])
