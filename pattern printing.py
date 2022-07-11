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
n = int(input("Enter the rows :: "))
n1=int(input("Enter your number :: "))
if (n1!=0 and n1!=1):
    {
        print("invalid input")
    }
elif n1 == 1:
    print("TRUE")
    for i in range(n):
            for j in range(i+1):
                     print("* ",end="")

            print("\n")
elif n1 == 0:
    print("FALSE")
    for i in range(n,0,-1):
            for j in range(i):
                     print("* ",end="")

            print("\n")

