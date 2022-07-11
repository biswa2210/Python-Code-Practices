# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import  combinations_with_replacement
if __name__=="__main__":
    line=input().split()
    word=line[0]
    word=list(word)
    word.sort()
    word=''.join(word)
    n=int(line[1])
    li=list(combinations_with_replacement(word,n))
    for elem in li:
        print(''.join(list(elem)))
