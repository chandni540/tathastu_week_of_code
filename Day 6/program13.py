n = int(input("\nEnter size of list : "))
li = []
for i in range(n):
    li.append(float(input("Enter elements :",i+1)))
print("\nProvided list :",li)
a=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            sum = li[i]+li[j]+li[k]
            if 0<sum<1:
                a=1
                print("The required triplet is: ({}, {}, {}), with sum={}".format(li[i],li[j],li[k],sum))

if a==0:
    print("No triplet!!")
