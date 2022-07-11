x=10
def func1():
    global x
    x=12
def go():
 x=88
 print(x)


print(x)
func1()
print(x)
go()
print(x)
def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()