def ackerman(a,b):
    if a==0:
        return b+1
    if b==0:
        return ackerman(a-1,1)
    
    x = ackerman(a,b-1)
    return ackerman(a-1,x)


a = int(input("Enter first value:"))
b = int(input("Enter second value:"))
print("\nThe computed ackerman value is:", ackerman(a,b))
