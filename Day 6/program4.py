def next(s):
    if s==sorted(s,reverse=True):
        return 'Already Largest'

    if s==sorted(s):
        s[len(s)-2] =s[len(s)-1]
        s[len(s)-1] = s[len(s)-2]
        str_num = [str(i) for i in s]
        return int("".join(str_num))

        
    for i in range(len(s)-1,0,-1):
        if s[i]>s[i-1]:
            position=i-1
            break
    
    small = s.index(min(filter(lambda i: i> s[position],s[position+1:])))
    x=s.pop(small)

    s.insert(position,x)
    s[position+1:] =sorted(s[position+1:]) 
    str_num = [str(i) for i in s]
    return int("".join(str_num))

num = list(map(int,input("Enter number:")))
print("\nThe next greatest number is : ",next(num))
