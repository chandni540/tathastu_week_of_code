def spiral(matrix):
    print("\nMatrix in spiral order: ")
    while matrix:
        for x in matrix.pop(0):
            print(x, end=" ")
        for v in matrix:
            print(v.pop(), end=" ")
        if matrix:
            for x in matrix.pop()[::-1]:
                print(x, end=" ")
        for v in matrix[::-1]:
            print(v.pop(0), end=" ")
            
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix = []

for i in range(row):
    a =[] 
    for j in range(col):
         a.append(int(input('Please enter the element   :  '))) 
    matrix.append(a)
print('The original matrix is : ',matrix)
spiral(matrix)
