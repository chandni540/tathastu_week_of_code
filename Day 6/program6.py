def sortRotate(l,n):
    minE = min(l)
    minI = l.index(minE)
    
    if l[0] == minE:
        print("List is not sorted and rotated")
        return
    
    if(l[0] < l[-1]):
        print("List is not sorted and rotated")
        flag=1
        return
    
    for i in range(1,size):
        if l[i] == minE:
            continue
        elif l[i] > l[i-1]:
            continue
        else:
            print("List is not sorted and rotated")
            return    	    
    print("List is sorted and rotated")	

n = int(input("Enter size of array: "))
l = []

for i in range(n):
    ls.append(int(input("Enter number " + str(i+1) + " : ")))
sortRot(l, n)	
