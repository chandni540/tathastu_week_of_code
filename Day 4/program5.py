n = int(input("Enter number of voters:"))
votes=[]
for i in range(n):
    name = input("Enter candidate's name:")
    votes.append(name)
dict={}
for i in votes:
    dict[i] = dict.get(i,0)+1

sorted_dict =sorted(dict.items(), key= lambda x:x[0], reverse=True)
win_cand = list(sorted(sorted_dict, key = lambda x:x[1]))

print("\nCandidate with maximum votes is:", win_cand[-1][0])
