n = int(input('enter the size of dictionary'))
dict = {}
for i in range(n):    
    key = input('\n Enter the key : ')
    dict[key] = int(input('Enter the value : '))
print("Second largest value in Dictonary:", list(sorted(dict.values()))[-2])
