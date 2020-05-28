n = int(input('Enter the number of sorted lists : '))
li = []

for i in range(n):
        i = []
        li.append(i)
    
for i in range(len(li)):
    m = int(input('\nEnter the size of list : ',i+1))
    for j in range(m):
        li[i].append(int(input('Enter the value for list : ',i+1)))
        
    li[i] = sorted(li[i])
    
print('\nThe merged sorted lists are : ',li)
list = []

for i in range(n):

    for j in range(len(li[i])):
          main.append(li[i][j])        
print('The sorted list is : ',sorted(list))
