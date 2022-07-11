def dec1(func1):
     def func2():
         print("EXECUTING PROGRAM")
         func1()
         print("EXECUTED")
     return func2()
@dec1
def hello():
    print("HELLO WORLD")
