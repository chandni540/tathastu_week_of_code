import random

n = int(input('Enter the length of array  :  '))
li = []

for i in range(n):
    li.append(random.randint(0,1))
print('\nThe list containing 0 and 1 is  : ',li)

x=0
y=0

for i in li:
    if i ==0:
        x+=1
    elif i==1:
        y+=1

li2 = []
for i in range(x):
    li2.append(0)
for i in range(y):
    li2.append(1)
print('\nThe sorted array is  : ',li2)
