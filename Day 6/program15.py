n = int(input("Enter size of array  :   "))
arr = []
for i in range(n):
    arr.append(int(input("Enter value  :  ")))
count = 0
print('\nThe array is : ',arr)
for i in range(1, n-1):
    flag = 0
    for j in range(i):
        if arr[j] > arr[i]:
            flag = 1
            break
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            flag = 1
            break
    if flag==0:
        print(arr[i],"  is the element which we are looking for.")
        count = 0
        break       
    else:
        count+=1        
if count != 0:        
    print("No such element found.")
