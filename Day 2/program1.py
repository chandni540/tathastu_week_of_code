num = int(input("Enter a number:"))

#odd/even
if(num % 2 == 0):
    print(num,"is an Even Number")
else:
    print(num,"is an Odd Number")

#prime
if num%2==0:
    print(num," is not a Prime number")
else:
    for i in range(2,num**0.5):
        if temp % a == 0:
            print(num,"is not a Prime Number")
            break
    else:
        print(num,"is a Prime Number")

#palindrome
word = str(num)
l = len(word)
for i in range(l // 2):
    if word[i] == word[l-i-1]:
        continue
    else:
        print(num," is not a Palindrome Number")
        break
else:
    print(num,"is a Palindrome Number")
    
#armstrong
sum = 0  
temp = num  
while temp > 0:  
    rem = temp % 10
    sum += rem ** 3  
    temp //= 10  
if num == sum:  
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")
