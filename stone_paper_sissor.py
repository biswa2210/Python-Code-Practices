#STONE PAPER SCISSORS --------------> GAME
import datetime
print("<---------------GAME---------------->")
print("\t\tSTONE--------->'S'\n\t\tPAPER--------->'P'\n\t\tSCISSORS------>'C")
print("<------------------------------------>")
print("SINGLE PLAYER FOR PRESS 1\nDOUBLE PLAYER FOR PRESS 2")
print("<------------------------------------>")
ch=int(input("enter your choice :: "))
print("\n--------------------->")

def single():
    j = 0
    m = 0
    pc = 0
    while(j<5):
        import random
        list = ["S", "P", "C"]
        choice = random.choice(list)
        t = input("your turn....('S','P','C')..-->")
        j=j+1
        if t == choice:
            print("...tie...")
            j=j-1
        elif (t=="S" and choice=="P"):
            print("ME-->STONE\nPC-->PAPER\nCOMPUTER IS WINNER")
            pc=pc+1
        elif (t=="S" and choice=="C"):
            print("ME-->STONE\nPC-->SCISSOR\nYOU ARE WINNER")
            m=m+1
        elif (t == "P" and choice == "S"):
            print("ME-->PAPER\nPC-->STONE\nYOU ARE WINNER")
            m = m + 1
        elif (t =="P" and choice == "C"):
            print("ME-->PAPER\nPC-->SCISSOR\nCOMPUTER IS WINNER")
            pc = pc + 1
        elif (t == "C" and choice == "P"):
            print("ME-->SCISSOR\nPC-->PAPER\nYOU ARE WINNER")
            m = m + 1
        elif (t == "C" and choice == "S"):
            print("ME-->SCISSOR\nPC-->STONE\nCOMPUTER IS WINNER")
            pc = pc + 1
        else:
            print("INVALID INPUT")
            j=j-1
    if pc==m:
        print("\n--------------------------> today's date and time is ::",datetime.datetime.now())
        print("\n---------------------------------->\nYOU...tie...COMPUTER\n---------------------------------->\n")
    elif pc > m:
        print("\n--------------------------> today's date and time is ::", datetime.datetime.now())

        print("\n---------------------------------->\nYOU WIN ",m," TIMES,","COMPUTER WINS ",pc," TIMES,SO COMPUTER IS WINNER\n---------------------------------->\n")
    else:
        print("\n--------------------------> today's date and time is ::", datetime.datetime.now())

        print("\n---------------------------------->\nCOMPUTER WINS ",pc," TIMES,","YOU WIN ",m," TIMES,SO YOU ARE WINNER\n---------------------------------->\n")
def double():
       t = input("1st player turn....('S','P','C')..-->")
       c = input("2nd player turn....('S','P','C')..-->")
       if t == c:
           print("...tie...")
       elif (t == "S" and c == "P"):
           print("1st player -->STONE\n2nd player -->PAPER\n2nd Player IS WINNER")
       elif (t == "S" and c == "C"):
           print("1st player -->STONE\n2nd player -->SCISSOR\n1st player  WINNER")
       elif (t == "P" and c == "S"):
           print("1st player -->PAPER\n2nd player -->STONE\n1st player WINNER")
       elif (t == "P" and c == "C"):
           print("1st player -->PAPER\n2nd player -->SCISSOR\n2nd player WINNER")
       elif (t == "C" and c == "P"):
           print("1st player -->SCISSOR\n2nd player -->PAPER\n1st player WINNER")
       elif (t == "C" and c == "S"):
           print("1st player -->SCISSOR\n2nd player -->STONE\n2nd player WINNER")
       else:
           print("INVALID INPUT")

if ch==1:
    single()
elif ch == 2:
    double()
else:
    print("INVALID INPUT")