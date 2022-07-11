from itertools import permutations
s,n=input().split(' ')
for i in list(permutations(sorted(s),int(n))):
    print("".join(i))