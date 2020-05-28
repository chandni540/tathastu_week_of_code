fib =list()
f,s=0,1
fib.append(f)
fib.append(s)
for i in range(50):
    t=f+s
    fib.append(t)
    f=s
    s=t
    
n = int(input("\nEnter the size :"))
li=[]
term_sum = 0
for i in range(n):
    elem=int(input("Enter element {}:".format(i+1)))
    li.append(elem)
    if elem in fibonnaci:
        sum+=elem

print("Given sequence:",li)
print("Sum of the Fibonnaci numbers is:",sum)

if(sum in fibonnaci):
    print(sum," is a Fibonnaci Number")

else:
    print(sum," is not a Fibonnaci Number")
