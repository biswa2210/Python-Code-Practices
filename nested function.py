def function1(): # outer function
    x = 2 # A variable defined within the outer function
    def function2(a): # inner function
       # Let's define a new variable within the inner function
       # rather than changing the value of x of the outer function
        x = 6
        print (a+x+x)
    print (x) # to display the value of x of the outer function
    function2(3)

function1()
#here function1 call 1st then call function2