n = int(input("Enter the size of tuple :"))
t_size = int(input("Enter the size of each tuple :"))

tup_list=[]
for i in range(n):
    list=[]
    print("\nEnter element of tuple :",i+1)
    for j in range(t_size):
        list.append(input())
    tup_list.append(tuple(list))

tup_list = tuple(tup_list)

pos=int(input("\nEnter index to sort by(< tuple_size):"))
sorted_list = sorted(tup_list,key= lambda x: x[pos])

print("The tuple sorted at ",pos,"is listed as:\n",sorted_list)
