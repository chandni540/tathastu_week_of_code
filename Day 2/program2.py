num = int(input("Enter the number of terms for the series : "))
a = 0
b = 1
print("The Fibonacci series is : ")
for i in range(num-1):
    print(a, end=", ")
    c = a + b
    a = b
    b = c
print(a)
