def fib(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

a=int(input("enter number of terms :: "))
x=0
for i in range(a):
   print(fib(x))
   x=x+1