def fact(a):
    fac=1
    for i in range(a):
        fac = fac * (i+1)
    return fac

n=int(input("enter the number :: "))
print(fact(n))
