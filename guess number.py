n=85
print("YOUR TOTAL CHANCE IS 9")
i=1
while(i<=9):
    inp=int(input("enter your number : "))
    if(inp>n):
        print("HAVE TO REDUCE IT,",end="")
    elif(inp<n):
        print("HAVE TO INCREASE IT,",end="")
    elif (inp == n):
        print("CONGO !!! YOU GOT IT,",end="")
        break
    else:
        print("INVALID INPUT",end="")
    print(9-i,"CHANCES ARE REMAINING")
    i=i+1