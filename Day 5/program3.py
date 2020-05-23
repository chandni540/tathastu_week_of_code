def steal(houseval, n): 
	if n == 0: 
		return 0
	if n == 1: 
		return houseval[0] 
	value2 = max(houseval[0], houseval[1]) 
	if n == 2: 
		return value2
	value1 = houseval[0]
	for i in range(2, n): 
		max_val = max(houseval[i]+value1, value2) 
		value1 = value2 
		value2 = max_val 

	return max_val 

n = int(input("Enter number of houses: "))
houseval = []
for i in range(n):
    houseval.append(int(input("House " + str(i+1) + " : ")))

print("Maximum possible stolen value :", steal(houseval, n)) 
