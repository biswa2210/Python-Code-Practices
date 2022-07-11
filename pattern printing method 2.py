#Pattern Printing
#input --> binary number
#if true-
#*
#**
#***
#****
#if false-
#****
#***
#**
#*

n=int(input("enter the no of rows :: "))
b=bool(int(input("please add 0 for false :: ")))
def star(n,b):
    i=1
    if b==True:
        while i<=n:
            print(i*"*")
            i=i+1
    else:
        while n>0:
            print(n*"*")
            n=n-1


star(n,b)