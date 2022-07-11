print("\n-------------------------------->\n* HEALTH MANAGEMENT SYSTEM *\n-------------------------------->\n\n<---------MENU--------->\n1.ADD RECORD\n2.CLIENT LIST\n3.EXIT\n<---------------------->")
def getdate():
    import datetime
    return datetime.datetime.now()#RETURN DATE AND TIME NOW
while(1):
    choice = int(input("Enter the number :: "))
    if choice==1:
        s1=input("ENTER CLIENT NAME :: ")
        sn=int(input("ENTER SERIAL NUMBER :: "))
        s2=input("ADD DIET AND EXERCISE :: ")
        f=open("add.txt","a")
        f.write("\n------------------------------------------------->")
        f.write("\nCLIENT NAME : ")
        f.write(s1)
        f.write("\nCLIENT SERIAL NUMBER : ")
        f.write(str(sn))
        f.write("\nADD DIET AND EXERCISE :: ")
        f.write(s2)
        s = getdate()
        f.write("\n")
        f.write(str(s))
        f.write("\n------------------------------------------------->\n")
        f.close()
        print(getdate())
    elif choice == 2:
        f = open("add.txt", "r")
        print(f.read())
        f.close()
    elif choice == 3:
           exit(1)
    else:
        print("INVALID INPUT")
