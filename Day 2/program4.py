n = int(input("Enter the value of N : "))
for i in range(n):
    print((n-i) * '*' + (i * 2) * ' ' + (n-i) * '*')
for i in range(n):
    print((i+1) * '*' + (2*(n- i - 1)) * ' ' + (i+1) * '*')
